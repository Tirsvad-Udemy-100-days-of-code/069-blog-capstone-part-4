"""
@file
@package tests.integration.test_routes
@brief Every route through the Flask test client against in-memory SQLite.
"""

import pytest
from flask import Flask
from flask.testing import FlaskClient

from blog.constants import SECRET_KEY_ENV_VAR, SEED_POSTS
from blog.domain.errors import PostNotFoundError
from blog.presentation.app import create_app
from blog.presentation.config import TESTING_CONFIG, default_config

VALID_FORM = {
    "title": "My new post",
    "subtitle": "About tests",
    "img_url": "https://example.com/a.jpg",
    "author": "Tester",
    "body": "<p>Hello <strong>world</strong></p>",
}


def test_get_all_posts_lists_seeded_posts(client: FlaskClient) -> None:
    """@brief The home page shows every seeded title and links to it."""
    response = client.get("/")
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    for item in SEED_POSTS:
        assert item["title"] in html
    assert "/post/1" in html
    assert "Clean Blog" in html


def test_get_all_posts_shows_message_when_no_posts(
    app: Flask, client: FlaskClient
) -> None:
    """@brief An empty blog shows a message instead of previews."""
    for post_id in (1, 2, 3):
        client.post(f"/delete/{post_id}")
    html = client.get("/").get_data(as_text=True)
    assert "There are no posts yet." in html


def test_show_post_renders_post_with_html_body(client: FlaskClient) -> None:
    """@brief The post page shows the title and the unescaped body."""
    response = client.get("/post/1")
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    assert SEED_POSTS[0]["title"] in html
    assert SEED_POSTS[0]["body"] in html


def test_show_post_returns_404_for_unknown_id(client: FlaskClient) -> None:
    """@brief An unknown post id gives the 404 page."""
    response = client.get("/post/999")
    assert response.status_code == 404
    assert "Post not found" in response.get_data(as_text=True)


def test_unknown_url_returns_404_page(client: FlaskClient) -> None:
    """@brief An unknown URL gives the same 404 page."""
    response = client.get("/no-such-page")
    assert response.status_code == 404
    assert "Post not found" in response.get_data(as_text=True)


def test_add_new_post_form_renders_all_fields(client: FlaskClient) -> None:
    """@brief The create page renders the form with the editor."""
    response = client.get("/new-post")
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    for name in ("title", "subtitle", "img_url", "author", "body", "submit"):
        assert f'name="{name}"' in html
    assert "ckeditor" in html.lower()


def test_add_new_post_stores_post_and_redirects(client: FlaskClient) -> None:
    """@brief A valid submission is saved and shown on the home page."""
    response = client.post("/new-post", data=VALID_FORM)
    assert response.status_code == 302
    assert response.headers["Location"] == "/"
    assert "My new post" in client.get("/").get_data(as_text=True)
    assert "<strong>world</strong>" in client.get("/post/4").get_data(as_text=True)


def test_add_new_post_strips_script_from_body(client: FlaskClient) -> None:
    """@brief A script in the body is removed before it is stored and shown."""
    data = {**VALID_FORM, "body": "<p>ok</p><script>alert(1)</script>"}
    client.post("/new-post", data=data)
    html = client.get("/post/4").get_data(as_text=True)
    assert "<p>ok</p>" in html
    assert "<script>alert(1)" not in html


def test_edit_post_strips_script_from_body(client: FlaskClient) -> None:
    """@brief A script added by an edit is removed too."""
    data = {**VALID_FORM, "body": '<p onclick="x()">ok</p><script>bad()</script>'}
    client.post("/edit-post/1", data=data)
    html = client.get("/post/1").get_data(as_text=True)
    assert "<script>bad()" not in html
    assert "onclick" not in html


def test_add_new_post_rejects_invalid_form(client: FlaskClient) -> None:
    """@brief An empty title shows the form again with the message."""
    data = {**VALID_FORM, "title": ""}
    response = client.post("/new-post", data=data)
    assert response.status_code == 200
    assert "This field is required." in response.get_data(as_text=True)
    assert client.get("/post/4").status_code == 404


def test_add_new_post_rejects_malformed_image_address(client: FlaskClient) -> None:
    """@brief An image address that is no URL or path is refused."""
    data = {**VALID_FORM, "img_url": "not a url"}
    response = client.post("/new-post", data=data)
    assert "Enter an http(s) address or a path." in response.get_data(as_text=True)
    assert client.get("/post/4").status_code == 404


def test_edit_post_form_is_prefilled(client: FlaskClient) -> None:
    """@brief The edit page holds the stored values."""
    html = client.get("/edit-post/1").get_data(as_text=True)
    assert SEED_POSTS[0]["title"] in html
    assert SEED_POSTS[0]["author"] in html


def test_edit_post_saves_changes_and_keeps_date(client: FlaskClient) -> None:
    """@brief A valid edit changes the text, redirects, and keeps the date."""
    response = client.post("/edit-post/1", data=VALID_FORM)
    assert response.status_code == 302
    assert response.headers["Location"] == "/post/1"
    html = client.get("/post/1").get_data(as_text=True)
    assert "My new post" in html
    assert SEED_POSTS[0]["date"] in html


def test_edit_post_rejects_invalid_form(client: FlaskClient) -> None:
    """@brief An invalid edit shows the form and changes nothing."""
    response = client.post("/edit-post/1", data={**VALID_FORM, "author": ""})
    assert response.status_code == 200
    assert SEED_POSTS[0]["title"] in client.get("/post/1").get_data(as_text=True)


def test_edit_post_returns_404_for_unknown_id(client: FlaskClient) -> None:
    """@brief Editing an unknown post gives 404 for GET and POST."""
    assert client.get("/edit-post/999").status_code == 404
    assert client.post("/edit-post/999", data=VALID_FORM).status_code == 404


def test_delete_post_removes_post_and_redirects(client: FlaskClient) -> None:
    """@brief A delete removes the post and returns to the home page."""
    response = client.post("/delete/2")
    assert response.status_code == 302
    assert response.headers["Location"] == "/"
    assert client.get("/post/2").status_code == 404
    assert client.get("/post/1").status_code == 200


def test_delete_post_returns_404_for_unknown_id(client: FlaskClient) -> None:
    """@brief Deleting an unknown post gives 404."""
    assert client.post("/delete/999").status_code == 404


def test_delete_post_rejects_get(client: FlaskClient) -> None:
    """@brief Deleting by GET is not allowed."""
    assert client.get("/delete/1").status_code == 405
    assert client.get("/post/1").status_code == 200


def test_delete_post_needs_csrf_token_when_csrf_enabled() -> None:
    """@brief With CSRF on, a delete without the token is refused."""
    app = create_app({**TESTING_CONFIG, "WTF_CSRF_ENABLED": True})
    client = app.test_client()
    assert client.post("/delete/1").status_code == 400
    assert client.get("/post/1").status_code == 200


def test_delete_forms_in_templates_carry_csrf_token() -> None:
    """@brief The delete control is a POST form with a CSRF token."""
    app = create_app({**TESTING_CONFIG, "WTF_CSRF_ENABLED": True})
    client = app.test_client()
    html = client.get("/post/1").get_data(as_text=True)
    assert 'action="/delete/1"' in html
    assert 'name="csrf_token"' in html


def test_about_page_renders(client: FlaskClient) -> None:
    """@brief The about page is served."""
    response = client.get("/about")
    assert response.status_code == 200
    assert "About Me" in response.get_data(as_text=True)


def test_contact_page_renders(client: FlaskClient) -> None:
    """@brief The contact page is served."""
    response = client.get("/contact")
    assert response.status_code == 200
    assert "Contact Me" in response.get_data(as_text=True)


def test_seed_runs_once_per_database(app: Flask) -> None:
    """@brief Creating the app again on the same data adds no posts."""
    from blog.infrastructure.post_repository import SqlAlchemyPostRepository
    from blog.infrastructure.seed import seed_posts_if_empty

    with app.app_context():
        assert seed_posts_if_empty(SqlAlchemyPostRepository()) == 0


def test_repository_raises_for_missing_and_unsaved_posts(app: Flask) -> None:
    """@brief The repository refuses unknown ids and posts without id."""
    from blog.domain.post import BlogPost
    from blog.infrastructure.post_repository import SqlAlchemyPostRepository

    repository = SqlAlchemyPostRepository()
    unsaved = BlogPost(None, "t", "s", "d", "b", "a", "/i")
    with app.app_context():
        with pytest.raises(PostNotFoundError):
            repository.get(999)
        with pytest.raises(PostNotFoundError):
            repository.update(unsaved)


def test_default_config_uses_secret_from_environment(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """@brief The secret key is read from the environment variable."""
    monkeypatch.setenv(SECRET_KEY_ENV_VAR, "from-env")
    assert default_config()["SECRET_KEY"] == "from-env"  # noqa: S105


def test_default_config_generates_random_secret_without_variable(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """@brief Without the variable each startup gets a new random key."""
    monkeypatch.delenv(SECRET_KEY_ENV_VAR, raising=False)
    first = default_config()["SECRET_KEY"]
    second = default_config()["SECRET_KEY"]
    assert isinstance(first, str)
    assert len(first) >= 32
    assert first != second
