"""
@file
@package tests.unit.test_html_sanitizer
@brief Tests of the bleach sanitizer adapter and its use in the use cases.
"""

from datetime import date

from blog.application.dto import PostContent
from blog.application.use_cases import CreatePost, EditPost
from blog.domain.user import User
from blog.infrastructure.html_sanitizer import BleachHtmlSanitizer
from tests.unit.fakes import FixedClock, InMemoryPostRepository

SANITIZER = BleachHtmlSanitizer()
AUTHOR = User(1, "admin@example.com", "hash", "Admin")


def test_sanitize_strips_script_tag() -> None:
    """@brief A script tag does not survive."""
    cleaned = SANITIZER.sanitize("<p>Hi</p><script>alert(1)</script>")
    assert "<script" not in cleaned
    assert "<p>Hi</p>" in cleaned


def test_sanitize_keeps_allowed_markup() -> None:
    """@brief CKEditor markup and allowed attributes are kept."""
    html = (
        "<h2>T</h2><p><strong>a</strong> <em>b</em> "
        '<a href="https://example.com" title="x">l</a></p>'
        '<ul><li>i</li></ul><img src="https://example.com/a.png" alt="p">'
    )
    assert SANITIZER.sanitize(html) == html


def test_sanitize_removes_event_handlers_and_unsafe_protocols() -> None:
    """@brief onclick attributes and javascript: links are dropped."""
    cleaned = SANITIZER.sanitize(
        '<a href="javascript:alert(1)" onclick="x()">l</a>'
        '<img src="https://e.com/a.png" onerror="x()">'
    )
    assert "javascript:" not in cleaned
    assert "onclick" not in cleaned
    assert "onerror" not in cleaned


def test_sanitize_keeps_mailto_link() -> None:
    """@brief A mailto link is allowed."""
    html = '<a href="mailto:a@example.com">mail</a>'
    assert SANITIZER.sanitize(html) == html


def test_sanitize_empty_string_stays_empty() -> None:
    """@brief Empty input gives empty output."""
    assert SANITIZER.sanitize("") == ""


def test_create_post_stores_sanitized_body() -> None:
    """@brief CreatePost stores only the cleaned body."""
    repository = InMemoryPostRepository()
    content = PostContent("t", "s", "/i.jpg", "<p>x</p><script>bad()</script>")
    use_case = CreatePost(repository, FixedClock(date(2026, 11, 5)), SANITIZER)
    post = use_case.execute(content, AUTHOR)
    assert "<script" not in post.body
    assert repository.get(1).body == post.body


def test_edit_post_stores_sanitized_body() -> None:
    """@brief EditPost stores only the cleaned body."""
    repository = InMemoryPostRepository()
    clock = FixedClock(date(2026, 11, 5))
    CreatePost(repository, clock, SANITIZER).execute(
        PostContent("t", "s", "/i.jpg", "<p>x</p>"), AUTHOR
    )
    edited = EditPost(repository, SANITIZER).execute(
        1, PostContent("t", "s", "/i.jpg", '<p onclick="x()">y</p>')
    )
    assert edited.body == "<p>y</p>"


def test_text_of_removes_all_tags() -> None:
    """@brief Only the text is left."""
    assert SANITIZER.text_of("<p>Hi <strong>you</strong></p>") == "Hi you"
