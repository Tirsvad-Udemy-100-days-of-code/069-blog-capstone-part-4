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


@pytest.fixture
def app() -> Iterator[Flask]:
    """
    @brief Build a fresh application with an in-memory database.
    @return The application, holding the three seeded posts; the database
            connection is closed after the test.
    """
    application = create_app(TESTING_CONFIG)
    yield application
    with application.app_context():
        db.session.remove()
        db.engine.dispose()


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """
    @brief Provide a test client.
    @param app The application.
    @return The client.
    """
    return app.test_client()
