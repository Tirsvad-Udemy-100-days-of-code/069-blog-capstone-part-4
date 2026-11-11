"""
@file
@package tests.integration.test_auth_routes
@brief Register, login and logout through the Flask test client.
"""

import pytest
from flask import Flask
from flask.testing import FlaskClient
from markupsafe import escape

from blog.constants import (
    FLASH_ALREADY_REGISTERED,
    FLASH_UNKNOWN_EMAIL,
    FLASH_WRONG_PASSWORD,
)
from blog.domain.errors import EmailAlreadyRegisteredError
from blog.domain.user import User
from blog.infrastructure.database import UserModel, db
from blog.infrastructure.user_repository import SqlAlchemyUserRepository
from blog.presentation.auth import LoginUser

SIGN_UP = {"email": "ann@example.com", "password": "secret", "name": "Ann"}
LOG_IN = {"email": "ann@example.com", "password": "secret"}


def _html(client: FlaskClient, url: str) -> str:
    """
    @brief Fetch a page.
    @param client The client.
    @param url The path.
    @return The page text.
    """
    return client.get(url).get_data(as_text=True)


def test_register_form_renders_fields(client: FlaskClient) -> None:
    """@brief The register page has the fields and the button."""
    html = _html(client, "/register")
    for name in ("email", "password", "name", "submit"):
        assert f'name="{name}"' in html
    assert "Sign Me Up!" in html


def test_login_form_renders_fields(client: FlaskClient) -> None:
    """@brief The login page has the fields and the button."""
    html = _html(client, "/login")
    for name in ("email", "password", "submit"):
        assert f'name="{name}"' in html
    assert "Let Me In!" in html


def test_register_stores_hash_and_logs_in(app: Flask, client: FlaskClient) -> None:
    """@brief Sign-up stores a hash, logs in and goes to the home page."""
    response = client.post("/register", data=SIGN_UP)
    assert response.status_code == 302
    assert response.headers["Location"] == "/"
    with app.app_context():
        row = db.session.scalars(db.select(UserModel)).one()
        assert row.email == "ann@example.com"
        assert row.password != "secret"
        assert "secret" not in row.password
        assert row.password.startswith("pbkdf2:sha256:")
    html = _html(client, "/")
    assert "Log Out" in html
    assert "Register" not in html


def test_register_rejects_invalid_form(client: FlaskClient) -> None:
    """@brief A malformed email shows the form again and stores nothing."""
    response = client.post("/register", data={**SIGN_UP, "email": "not-an-email"})
    assert response.status_code == 200
    assert "Enter a valid email address." in response.get_data(as_text=True)
    assert "Log Out" not in _html(client, "/")


def test_register_duplicate_email_flashes_and_redirects_to_login(
    client: FlaskClient,
) -> None:
    """@brief A known email sends the visitor to the login page with a message."""
    client.post("/register", data=SIGN_UP)
    client.get("/logout")
    response = client.post("/register", data=SIGN_UP)
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"
    assert str(escape(FLASH_ALREADY_REGISTERED)) in _html(client, "/login")


def test_login_success_redirects_home_and_shows_log_out(client: FlaskClient) -> None:
    """@brief The right credentials log the user in."""
    client.post("/register", data=SIGN_UP)
    client.get("/logout")
    response = client.post("/login", data=LOG_IN)
    assert response.status_code == 302
    assert response.headers["Location"] == "/"
    assert "Log Out" in _html(client, "/")


def test_login_unknown_email_flashes_message(client: FlaskClient) -> None:
    """@brief An unknown email shows its own message."""
    response = client.post("/login", data=LOG_IN)
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    assert FLASH_UNKNOWN_EMAIL in html
    assert FLASH_WRONG_PASSWORD not in html
    assert "Log Out" not in html


def test_login_wrong_password_flashes_message(client: FlaskClient) -> None:
    """@brief A wrong password shows a different message."""
    client.post("/register", data=SIGN_UP)
    client.get("/logout")
    response = client.post("/login", data={**LOG_IN, "password": "wrong"})
    html = response.get_data(as_text=True)
    assert FLASH_WRONG_PASSWORD in html
    assert FLASH_UNKNOWN_EMAIL not in html
    assert "Log Out" not in _html(client, "/")


def test_login_ignores_next_parameter(client: FlaskClient) -> None:
    """@brief A next parameter cannot redirect to another site."""
    client.post("/register", data=SIGN_UP)
    client.get("/logout")
    response = client.post("/login?next=https://evil.example/", data=LOG_IN)
    assert response.headers["Location"] == "/"


def test_logout_ends_session_and_redirects_home(client: FlaskClient) -> None:
    """@brief Logging out shows Login and Register again."""
    client.post("/register", data=SIGN_UP)
    response = client.get("/logout")
    assert response.status_code == 302
    assert response.headers["Location"] == "/"
    html = _html(client, "/")
    assert "Log Out" not in html
    assert 'href="/login"' in html


def test_navigation_shows_login_and_register_when_anonymous(
    client: FlaskClient,
) -> None:
    """@brief A visitor sees Login and Register, not Log Out."""
    html = _html(client, "/")
    assert 'href="/login"' in html
    assert 'href="/register"' in html
    assert "Log Out" not in html


def test_stale_session_user_is_treated_as_anonymous(client: FlaskClient) -> None:
    """@brief A session naming a missing or malformed user id is anonymous."""
    with client.session_transaction() as session:
        session["_user_id"] = "999"
    assert "Log Out" not in _html(client, "/")
    with client.session_transaction() as session:
        session["_user_id"] = "abc"
    assert "Log Out" not in _html(client, "/")


def test_user_repository_rejects_duplicate_email(app: Flask) -> None:
    """@brief The unique column maps to the domain error."""
    repository = SqlAlchemyUserRepository()
    user = User(None, "a@example.com", "hash", "A")
    with app.app_context():
        repository.add(user)
        with pytest.raises(EmailAlreadyRegisteredError):
            repository.add(user)
        assert repository.get_by_id(1) is not None
        assert repository.get_by_email("a@example.com") is not None
        assert repository.get_by_id(2) is None


def test_posts_are_not_changed_by_registering(client: FlaskClient) -> None:
    """@brief Signing up leaves the posts as they were."""
    client.post("/register", data=SIGN_UP)
    assert _html(client, "/").count("post-title") == 3


def test_login_user_rejects_unsaved_user() -> None:
    """@brief A user without id cannot be put in a session."""
    with pytest.raises(ValueError, match="id"):
        LoginUser(User(None, "a@example.com", "hash", "A"))
