"""
@file
@package blog.presentation.auth
@brief Flask-Login wiring: the session user adapter and the user loader.
"""

from flask import Flask
from flask_login import LoginManager, UserMixin

from blog.domain.user import User
from blog.presentation.services import current_use_cases


class LoginUser(UserMixin):  # type: ignore[misc]
    """@brief Adapts a domain user to what Flask-Login needs."""

    def __init__(self, user: User) -> None:
        """
        @brief Wrap a stored user.
        @param user The user; it must have an id.
        """
        if user.id is None:
            raise ValueError("A logged in user has an id")
        self.user = user
        self.id = user.id

    def get_id(self) -> str:
        """
        @brief Give the id stored in the session.
        @return The user id as text.
        """
        return str(self.id)


def load_login_user(user_id: str) -> LoginUser | None:
    """
    @brief Find the user of a session.
    @param user_id The id stored in the session.
    @return The user, or None when the id is stale or malformed.
    """
    if not user_id.isdecimal():
        return None
    user = current_use_cases().get_user.execute(int(user_id))
    return None if user is None else LoginUser(user)


def init_login_manager(app: Flask) -> None:
    """
    @brief Attach Flask-Login to the application.
    @param app The application.
    """
    manager = LoginManager()
    manager.login_view = "login"
    manager.user_loader(load_login_user)
    manager.init_app(app)
