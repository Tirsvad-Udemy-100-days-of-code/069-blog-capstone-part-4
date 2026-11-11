"""
@file
@package blog.presentation.app
@brief The application factory and composition root.
"""

from collections.abc import Mapping
from pathlib import Path

from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_wtf import CSRFProtect

from blog.application.use_cases import (
    CreatePost,
    DeletePost,
    EditPost,
    GetPost,
    ListPosts,
)
from blog.constants import INSTANCE_DIR_NAME
from blog.infrastructure.clock import SystemClock
from blog.infrastructure.database import db
from blog.infrastructure.html_sanitizer import BleachHtmlSanitizer
from blog.infrastructure.post_repository import SqlAlchemyPostRepository
from blog.infrastructure.seed import seed_posts_if_empty
from blog.presentation.config import default_config
from blog.presentation.routes import USE_CASES_KEY, register_routes
from blog.presentation.services import UseCases


def create_app(config: Mapping[str, object] | None = None) -> Flask:
    """
    @brief Build the application; the one place that creates the adapters.
    @param config Settings that replace the defaults (for example the testing
           configuration); None keeps the defaults.
    @return The application, with its tables created and example posts seeded.
    """
    app = Flask(
        __name__,
        instance_path=str(Path.cwd() / INSTANCE_DIR_NAME),
    )
    app.config.from_mapping(default_config())
    if config is not None:
        app.config.from_mapping(config)

    db.init_app(app)
    CSRFProtect(app)
    Bootstrap5(app)
    CKEditor(app)

    repository = SqlAlchemyPostRepository()
    sanitizer = BleachHtmlSanitizer()
    app.extensions[USE_CASES_KEY] = UseCases(
        list_posts=ListPosts(repository),
        get_post=GetPost(repository),
        create_post=CreatePost(repository, SystemClock(), sanitizer),
        edit_post=EditPost(repository, sanitizer),
        delete_post=DeletePost(repository),
    )
    register_routes(app)

    with app.app_context():
        db.create_all()
        seed_posts_if_empty(repository)
    return app
