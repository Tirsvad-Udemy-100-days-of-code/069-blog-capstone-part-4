"""
@file
@package tests.integration.test_routes
@brief The post routes as the admin, through the Flask test client.
"""

import pytest
from flask import Flask
from flask.testing import FlaskClient

from blog.constants import SECRET_KEY_ENV_VAR
from blog.presentation.config import default_config
from tests.integration.conftest import ADMIN_NAME, POST_TITLES, post_form


def test_get_all_posts_lists_posts_with_author(
    app_with_posts: Flask, client: FlaskClient
) -> None:
    """@brief The home page shows every title, the author name and links."""
    response = client.get("/")
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    for title in POST_TITLES:
        assert title in html
    assert f"Posted by {ADMIN_NAME}" in html
    assert "/post/1" in html
    assert "Clean Blog" in html


def test_get_all_posts_shows_empty_state_without_posts(client: FlaskClient) -> None:
    """@brief A new blog shows "No posts yet"."""
    html = client.get("/").get_data(as_text=True)
    assert "No posts yet" in html
    assert "post-title" not in html


def test_show_post_renders_post_with_html_body_and_author(
    app_with_posts: Flask, client: FlaskClient
) -> None:
    """@brief The post page shows the title, author name and the body markup."""
    response = client.get("/post/1")
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "First post" in html
    assert f"Posted by {ADMIN_NAME}" in html
    assert "<p>Hello</p>" in html


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


def test_add_new_post_form_renders_fields_without_author(
    admin_client: FlaskClient,
) -> None:
    """@brief The create page renders the form and the editor, with no author."""
    html = admin_client.get("/new-post").get_data(as_text=True)
    for name in ("title", "subtitle", "img_url", "body", "submit"):
        assert f'name="{name}"' in html
    assert 'name="author"' not in html
    assert "ckeditor" in html.lower()


def test_add_new_post_stores_post_with_admin_as_author(
    admin_client: FlaskClient, client: FlaskClient
) -> None:
    """@brief A valid submission is saved with the logged in user as author."""
    response = admin_client.post("/new-post", data=post_form())
    assert response.status_code == 302
    assert response.headers["Location"] == "/"
    html = client.get("/post/1").get_data(as_text=True)
    assert "My new post" in html
    assert f"Posted by {ADMIN_NAME}" in html


def test_add_new_post_rejects_invalid_form(
    admin_client: FlaskClient, client: FlaskClient
) -> None:
    """@brief An empty title shows the form again with the message."""
    response = admin_client.post("/new-post", data={**post_form(), "title": ""})
    assert response.status_code == 200
    assert "This field is required." in response.get_data(as_text=True)
    assert client.get("/post/1").status_code == 404


def test_add_new_post_rejects_malformed_image_address(
    admin_client: FlaskClient, client: FlaskClient
) -> None:
    """@brief An image address that is no URL or path is refused."""
    data = {**post_form(), "img_url": "not a url"}
    response = admin_client.post("/new-post", data=data)
    assert "Enter an http(s) address or a path." in response.get_data(as_text=True)
    assert client.get("/post/1").status_code == 404


def test_add_new_post_strips_script_from_body(
    admin_client: FlaskClient, client: FlaskClient
) -> None:
    """@brief A script in the body is removed before it is stored and shown."""
    body = "<p>ok</p><script>alert(1)</script>"
    admin_client.post("/new-post", data=post_form(body=body))
    html = client.get("/post/1").get_data(as_text=True)
    assert "<p>ok</p>" in html
    assert "<script>alert(1)" not in html


def test_edit_post_form_is_prefilled(
    app_with_posts: Flask, admin_client: FlaskClient
) -> None:
    """@brief The edit page holds the stored values."""
    html = admin_client.get("/edit-post/1").get_data(as_text=True)
    assert "First post" in html
    assert 'name="author"' not in html


def test_edit_post_saves_changes_and_keeps_date_and_author(
    app_with_posts: Flask, admin_client: FlaskClient, client: FlaskClient
) -> None:
    """@brief A valid edit changes the text but not the author."""
    before = client.get("/post/1").get_data(as_text=True)
    response = admin_client.post("/edit-post/1", data=post_form("Changed title"))
    assert response.status_code == 302
    assert response.headers["Location"] == "/post/1"
    html = client.get("/post/1").get_data(as_text=True)
    assert "Changed title" in html
    assert f"Posted by {ADMIN_NAME}" in html
    date_text = before.split(" on ")[1].split("<")[0]
    assert date_text in html


def test_edit_post_strips_script_from_body(
    app_with_posts: Flask, admin_client: FlaskClient, client: FlaskClient
) -> None:
    """@brief A script added by an edit is removed too."""
    body = '<p onclick="x()">ok</p><script>bad()</script>'
    admin_client.post("/edit-post/1", data=post_form(body=body))
    html = client.get("/post/1").get_data(as_text=True)
    assert "<script>bad()" not in html
    assert "onclick" not in html


def test_edit_post_rejects_invalid_form(
    app_with_posts: Flask, admin_client: FlaskClient, client: FlaskClient
) -> None:
    """@brief An invalid edit shows the form and changes nothing."""
    data = {**post_form(), "subtitle": ""}
    response = admin_client.post("/edit-post/1", data=data)
    assert response.status_code == 200
    assert "First post" in client.get("/post/1").get_data(as_text=True)


def test_edit_post_returns_404_for_unknown_id(admin_client: FlaskClient) -> None:
    """@brief The admin editing an unknown post gets 404 for GET and POST."""
    assert admin_client.get("/edit-post/999").status_code == 404
    assert admin_client.post("/edit-post/999", data=post_form()).status_code == 404


def test_delete_post_removes_post_and_redirects(
    app_with_posts: Flask, admin_client: FlaskClient, client: FlaskClient
) -> None:
    """@brief A delete removes the post and returns to the home page."""
    response = admin_client.post("/delete/2")
    assert response.status_code == 302
    assert response.headers["Location"] == "/"
    assert client.get("/post/2").status_code == 404
    assert client.get("/post/1").status_code == 200


def test_delete_post_returns_404_for_unknown_id(admin_client: FlaskClient) -> None:
    """@brief The admin deleting an unknown post gets 404."""
    assert admin_client.post("/delete/999").status_code == 404


def test_delete_post_rejects_get(
    app_with_posts: Flask, admin_client: FlaskClient
) -> None:
    """@brief Deleting by GET is not allowed, even for the admin."""
    assert admin_client.get("/delete/1").status_code == 405
    assert admin_client.get("/post/1").status_code == 200


def test_delete_post_needs_csrf_token_when_csrf_enabled(csrf_app: Flask) -> None:
    """@brief With CSRF on, a delete without the token is refused."""
    assert csrf_app.test_client().post("/delete/1").status_code == 400


def test_delete_forms_carry_csrf_token(
    app_with_posts: Flask, admin_client: FlaskClient
) -> None:
    """@brief The delete control is a POST form with a CSRF token."""
    html = admin_client.get("/post/1").get_data(as_text=True)
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
