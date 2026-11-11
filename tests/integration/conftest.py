"""
@file
@package tests.integration.conftest
@brief Application and client fixtures for the integration tests.
"""

from collections.abc import Iterator

import pytest
from flask import Flask
from flask.testing import FlaskClient

from blog.infrastructure.database import db
from blog.presentation.app import create_app
from blog.presentation.config import TESTING_CONFIG

ADMIN_NAME = "Admin Annie"
MEMBER_NAME = "Member Max"
POST_TITLES = ("First post", "Second post", "Third post")


def post_form(title: str = "My new post", body: str = "<p>Hello</p>") -> dict[str, str]:
    """
    @brief Build valid post form data.
    @param title The post title.
    @param body The post body.
    @return Form fields for the create and edit routes.
    """
    return {
        "title": title,
        "subtitle": "About tests",
        "img_url": "https://example.com/a.jpg",
        "body": body,
    }


def sign_up(client: FlaskClient, email: str, name: str) -> None:
    """
    @brief Register a user through the form; the client is then logged in.
    @param client The client.
    @param email The email.
    @param name The name.
    """
    client.post("/register", data={"email": email, "password": "secret", "name": name})


@pytest.fixture
def app() -> Iterator[Flask]:
    """
    @brief Build a fresh application with an empty in-memory database.
    @return The application; the database connection is closed after the test.
    """
    application = create_app(TESTING_CONFIG)
    yield application
    with application.app_context():
        db.session.remove()
        db.engine.dispose()


@pytest.fixture
def csrf_app() -> Iterator[Flask]:
    """
    @brief Build an application that checks CSRF tokens, as in production.
    @return The application; the database connection is closed after the test.
    """
    application = create_app({**TESTING_CONFIG, "WTF_CSRF_ENABLED": True})
    yield application
    with application.app_context():
        db.session.remove()
        db.engine.dispose()


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """
    @brief Provide an anonymous test client.
    @param app The application.
    @return The client.
    """
    return app.test_client()


@pytest.fixture
def admin_client(app: Flask) -> FlaskClient:
    """
    @brief Register the first user (the admin) and keep the client logged in.
    @param app The application.
    @return The client of the admin.
    """
    admin = app.test_client()
    sign_up(admin, "admin@example.com", ADMIN_NAME)
    return admin


@pytest.fixture
def app_with_posts(app: Flask, admin_client: FlaskClient) -> Flask:
    """
    @brief Let the admin write three posts, with ids 1 to 3.
    @param app The application.
    @param admin_client The admin.
    @return The application.
    """
    for title in POST_TITLES:
        admin_client.post("/new-post", data=post_form(title))
    return app


@pytest.fixture
def member_client(app_with_posts: Flask) -> FlaskClient:
    """
    @brief Register a second user (not the admin) and keep the client logged in.
    @param app_with_posts The application with posts.
    @return The client of the member.
    """
    member = app_with_posts.test_client()
    sign_up(member, "member@example.com", MEMBER_NAME)
    return member
