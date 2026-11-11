"""
@file
@package blog.presentation.authorisation
@brief Who is logged in, and the admin_only guard for routes.
"""

from collections.abc import Callable
from functools import wraps

from flask import abort
from flask_login import current_user

from blog.domain.user import User, is_admin
from blog.presentation.auth import LoginUser


def current_domain_user() -> User | None:
    """
    @brief Read the logged in user.
    @return The domain user, or None for a visitor who is not logged in.
    """
    if not current_user.is_authenticated:
        return None
    login_user: LoginUser = current_user._get_current_object()  # noqa: SLF001
    return login_user.user


def current_user_is_admin() -> bool:
    """
    @brief Tell whether the logged in user is the admin.
    @return True only for the admin.
    """
    return is_admin(current_domain_user())


def admin_only[**Params, Result](
    view: Callable[Params, Result],
) -> Callable[Params, Result]:
    """
    @brief Guard a view so that only the admin may run it.
    @param view The view function.
    @return The guarded view; anyone else gets HTTP 403.
    """

    @wraps(view)
    def guarded(*args: Params.args, **kwargs: Params.kwargs) -> Result:
        """
        @brief Run the view for the admin, or refuse.
        @param args Positional arguments of the view.
        @param kwargs Keyword arguments of the view.
        @return The result of the view.
        """
        if not current_user_is_admin():
            abort(403)
        return view(*args, **kwargs)

    return guarded
