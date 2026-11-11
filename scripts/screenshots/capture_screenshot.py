"""@file
@brief Capture the screenshots of the blog with a headless browser.

Runs inside the Docker container started by capture_screenshot.sh, never on the
host desktop. One fresh database is filled with example data, the blog is
started on it, and each step takes one PNG file into /out.
"""

import html
import secrets
import socket
import sqlite3
import subprocess
import sys
import threading
from collections.abc import Callable
from pathlib import Path

from playwright.sync_api import Browser, Page, sync_playwright

SCRIPTS_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = Path("/out")
DATABASE_PATH = Path("instance/blog.db")
HOST = "127.0.0.1"
PORT = 5002
BASE_URL = f"http://{HOST}:{PORT}"
VIEWPORT = {"width": 1000, "height": 640}
EXAMPLE_PASSWORD = "example-password-1"  # noqa: S105  (example data, not a secret)
IMAGE_TIMEOUT_MS = 15000
START_ATTEMPTS = 100
START_PAUSE_SECONDS = 0.3


def wait_for_server(server: subprocess.Popen[bytes]) -> None:
    """@brief Wait until the blog answers on its port.

    @param server The running blog process.
    """
    pause = threading.Event()
    for _ in range(START_ATTEMPTS):
        if server.poll() is not None:
            break
        try:
            socket.create_connection((HOST, PORT), timeout=1).close()
        except OSError:
            pause.wait(START_PAUSE_SECONDS)
        else:
            return
    raise RuntimeError("The blog did not start.")


def settle(page: Page) -> None:
    """@brief Wait until the page, its scripts and its images have loaded.

    @param page The browser page.
    """
    page.wait_for_load_state("networkidle")
    page.wait_for_function(
        "Array.from(document.images).every(i => i.complete)",
        timeout=IMAGE_TIMEOUT_MS,
    )


def wait_for_editor(page: Page) -> None:
    """@brief Wait until CKEditor has replaced the comment text area.

    @param page The browser page.
    """
    page.wait_for_function(
        "window.CKEDITOR && CKEDITOR.instances.comment_text"
        " && CKEDITOR.instances.comment_text.status === 'ready'",
        timeout=IMAGE_TIMEOUT_MS,
    )


def snap(page: Page, name: str, *, full_page: bool = True) -> None:
    """@brief Take the screenshot of a page.

    @param page The browser page.
    @param name File name without the extension.
    @param full_page True to include the part below the window.
    """
    settle(page)
    page.screenshot(path=str(OUTPUT_DIR / f"{name}.png"), full_page=full_page)


def log_in(page: Page, email: str, password: str) -> None:
    """@brief Log in through the login form.

    @param page The browser page.
    @param email Email of the example user.
    @param password Password to type.
    """
    page.goto(f"{BASE_URL}/login")
    page.fill("#email", email)
    page.fill("#password", password)
    page.click("#submit")
    page.wait_for_load_state("load")


def step_register(browser: Browser) -> None:
    """@brief Register page with example values typed in and the password masked.

    @param browser The browser.
    """
    page = browser.new_page(viewport=VIEWPORT)
    page.goto(f"{BASE_URL}/register")
    page.fill("#email", "jane@example.com")
    page.fill("#password", EXAMPLE_PASSWORD)
    page.fill("#name", "Jane Doe")
    snap(page, "step-01-register-form")


def step_login_form(browser: Browser) -> None:
    """@brief Login page filled in.

    @param browser The browser.
    """
    page = browser.new_page(viewport=VIEWPORT)
    page.goto(f"{BASE_URL}/login")
    page.fill("#email", "jane@example.com")
    page.fill("#password", EXAMPLE_PASSWORD)
    snap(page, "step-02a-login-form")


def step_login_wrong_password(browser: Browser) -> None:
    """@brief Login page after a wrong password, with the flash message.

    @param browser The browser.
    """
    page = browser.new_page(viewport=VIEWPORT)
    log_in(page, "jane@example.com", "wrong-password")
    snap(page, "step-02b-login-wrong-password")


def step_admin_home(browser: Browser) -> None:
    """@brief Home page of the admin, with the Create, Edit and Delete controls.

    @param browser The browser.
    """
    page = browser.new_page(viewport=VIEWPORT)
    log_in(page, "jane@example.com", EXAMPLE_PASSWORD)
    snap(page, "step-03a-admin-home")


def step_member_home(browser: Browser) -> None:
    """@brief Home page of a member, without the admin controls.

    @param browser The browser.
    """
    page = browser.new_page(viewport=VIEWPORT)
    log_in(page, "john@example.com", EXAMPLE_PASSWORD)
    snap(page, "step-03b-member-home")


def step_forbidden(browser: Browser) -> None:
    """@brief A member who opens the new-post page sees the 403 page.

    @param browser The browser.
    """
    page = browser.new_page(viewport=VIEWPORT)
    log_in(page, "john@example.com", EXAMPLE_PASSWORD)
    page.goto(f"{BASE_URL}/new-post")
    snap(page, "step-03c-403-forbidden")


def format_table(headers: list[str], rows: list[tuple[object, ...]]) -> str:
    """@brief Lay out rows as a text table, like the sqlite3 shell does.

    @param headers Column names.
    @param rows Values of each row.
    @return The table as text.
    """
    cells = [[str(value) for value in row] for row in rows]
    widths = [
        max(len(header), *(len(row[i]) for row in cells))
        for i, header in enumerate(headers)
    ]
    line = "  ".join(header.ljust(widths[i]) for i, header in enumerate(headers))
    rule = "  ".join("-" * width for width in widths)
    body = ["  ".join(v.ljust(widths[i]) for i, v in enumerate(row)) for row in cells]
    return "\n".join([line, rule, *body])


# Each query is a fixed text of this script; no user input reaches the database.
QUERIES = (
    (
        "users",
        "SELECT id, name, email, substr(password, 1, 20) || '...' AS password"
        " FROM users",
    ),
    ("blog_posts", "SELECT id, title, author_id FROM blog_posts"),
    (
        "comments",
        "SELECT id, author_id, post_id, substr(text, 1, 40) AS text FROM comments",
    ),
    (
        "who wrote each post",
        "SELECT p.id AS post_id, p.title, u.name AS author"
        " FROM blog_posts p JOIN users u ON u.id = p.author_id",
    ),
    (
        "who commented on post 1",
        "SELECT c.id, u.name AS commenter, c.post_id"
        " FROM comments c JOIN users u ON u.id = c.author_id WHERE c.post_id = 1",
    ),
)


def query_report() -> str:
    """@brief Run the queries on the example database and format the answer.

    @return Text that looks like a terminal session.
    """
    lines = [f"$ sqlite3 -header {DATABASE_PATH}"]
    with sqlite3.connect(DATABASE_PATH) as connection:
        for title, sql in QUERIES:
            cursor = connection.execute(sql)
            headers = [column[0] for column in cursor.description]
            lines += ["", f"-- {title}", f"sqlite> {sql};", ""]
            lines.append(format_table(headers, cursor.fetchall()))
    return "\n".join(lines)


def step_database_relations(browser: Browser) -> None:
    """@brief Terminal-style page with real queries on the relations.

    @param browser The browser.
    """
    page_html = (
        "<body style='font-family:monospace;font-size:12px;background:#1e1e1e;"
        "color:#ddd;padding:16px'><h3 style='color:#9cdcfe'>"
        "Users, posts and comments in blog.db</h3><pre>"
        + html.escape(query_report())
        + "</pre></body>"
    )
    page = browser.new_page(viewport=VIEWPORT)
    page.set_content(page_html)
    snap(page, "step-04-database-relations")


def step_comment_form(browser: Browser) -> None:
    """@brief A member on the post page with the comment form.

    @param browser The browser.
    """
    page = browser.new_page(viewport=VIEWPORT)
    log_in(page, "john@example.com", EXAMPLE_PASSWORD)
    page.goto(f"{BASE_URL}/post/1")
    wait_for_editor(page)
    page.evaluate(
        "CKEDITOR.instances.comment_text.setData("
        "'<p>Cacti are fascinating. Thanks for sharing!</p>')"
    )
    page.locator(".cke").first.scroll_into_view_if_needed()
    snap(page, "step-05a-comment-form", full_page=False)


def step_comment_login_required(browser: Browser) -> None:
    """@brief A visitor who submits a comment is sent to the login page.

    @param browser The browser.
    """
    page = browser.new_page(viewport=VIEWPORT)
    page.goto(f"{BASE_URL}/post/1")
    wait_for_editor(page)
    page.evaluate("CKEDITOR.instances.comment_text.setData('<p>Nice post!</p>')")
    page.click("#submit")
    page.wait_for_url(f"{BASE_URL}/login")
    snap(page, "step-05b-comment-login-required")


def step_comments_list(browser: Browser) -> None:
    """@brief The post page with its three comments.

    @param browser The browser.
    """
    page = browser.new_page(viewport=VIEWPORT)
    page.goto(f"{BASE_URL}/post/1")
    snap(page, "step-05c-comments-list")


def step_gravatar(browser: Browser) -> None:
    """@brief The comments region with the Gravatar avatars.

    @param browser The browser.
    """
    page = browser.new_page(viewport=VIEWPORT)
    page.goto(f"{BASE_URL}/post/1")
    settle(page)
    loaded = page.evaluate(
        "Array.from(document.querySelectorAll('li img')).every(i => i.naturalWidth > 0)"
    )
    print(f"Gravatar images loaded: {loaded}")
    page.locator("ul.list-unstyled").screenshot(
        path=str(OUTPUT_DIR / "step-06-gravatar-avatars.png")
    )


STEPS: dict[str, Callable[[Browser], None]] = {
    "step-01-register-form": step_register,
    "step-02a-login-form": step_login_form,
    "step-02b-login-wrong-password": step_login_wrong_password,
    "step-03a-admin-home": step_admin_home,
    "step-03b-member-home": step_member_home,
    "step-03c-403-forbidden": step_forbidden,
    "step-04-database-relations": step_database_relations,
    "step-05a-comment-form": step_comment_form,
    "step-05b-comment-login-required": step_comment_login_required,
    "step-05c-comments-list": step_comments_list,
    "step-06-gravatar-avatars": step_gravatar,
}
"""@brief Every screenshot step, in the order of the lecture."""


def main() -> None:
    """@brief Seed a new database, start the blog, and run the wanted steps."""
    wanted = sys.argv[1:]
    names = [n for n in STEPS if "--all" in wanted or n in wanted]
    if not names:
        raise SystemExit("Name a step, or use --all. Steps: " + ", ".join(STEPS))
    # Fixed command inside the container: this interpreter and a script of this folder.
    # nosemgrep: opengrep.selected-rules.python.lang.security.audit.dangerous-subprocess-use-audit  # noqa: E501
    subprocess.run(  # noqa: S603
        [sys.executable, str(SCRIPTS_DIR / "seed_example_data.py")], check=True
    )
    environment = {
        "BLOG_SECRET_KEY": secrets.token_hex(),
        "PATH": "/usr/local/bin:/usr/bin:/bin",
    }
    # nosemgrep: opengrep.selected-rules.python.lang.security.audit.dangerous-subprocess-use-audit  # noqa: E501
    server = subprocess.Popen([sys.executable, "-m", "blog"], env=environment)  # noqa: S603
    try:
        wait_for_server(server)
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            for name in names:
                STEPS[name](browser)
            browser.close()
    finally:
        server.terminate()
        server.wait()


if __name__ == "__main__":
    main()
