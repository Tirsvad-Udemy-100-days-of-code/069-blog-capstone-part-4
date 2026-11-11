"""
@file
@package tests.integration.test_app_factory
@brief Tests of the composition root, the entry point and small adapters.
"""

from datetime import date
from pathlib import Path

import pytest

from blog import __main__ as entry_point
from blog.constants import DATABASE_FILE_NAME, DEFAULT_HOST, DEFAULT_PORT
from blog.domain.post import BlogPost
from blog.domain.user import User
from blog.infrastructure.clock import SystemClock
from blog.infrastructure.database import db
from blog.presentation.app import create_app
from blog.presentation.view_models import to_post_view_model


def test_create_app_default_creates_database_file_in_instance_folder(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """@brief Without a config the database file lives in instance/."""
    monkeypatch.chdir(tmp_path)
    app = create_app()
    assert (tmp_path / "instance" / DATABASE_FILE_NAME).is_file()
    assert app.test_client().get("/").status_code == 200
    with app.app_context():
        db.session.remove()
        db.engine.dispose()


def test_main_runs_server_on_default_host_and_port(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """@brief The entry point starts the app on 127.0.0.1:5002."""
    calls: list[tuple[str, int]] = []

    class FakeApp:
        """@brief Records the run call."""

        def run(self, host: str, port: int) -> None:
            """
            @brief Record the arguments.
            @param host The host.
            @param port The port.
            """
            calls.append((host, port))

    monkeypatch.setattr(entry_point, "create_app", FakeApp)
    entry_point.main()
    assert calls == [(DEFAULT_HOST, DEFAULT_PORT)]
    assert (DEFAULT_HOST, DEFAULT_PORT) == ("127.0.0.1", 5002)


def test_system_clock_returns_a_date() -> None:
    """@brief The system clock tells a date."""
    assert isinstance(SystemClock().today(), date)


def test_to_post_view_model_rejects_unsaved_post() -> None:
    """@brief A post without id cannot be shown."""
    with pytest.raises(ValueError, match="id"):
        to_post_view_model(
            BlogPost(None, "t", "s", "d", "b", User(1, "a@b.c", "h", "A"), "/i")
        )
