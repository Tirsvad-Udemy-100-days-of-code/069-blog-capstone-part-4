"""
@file
@package blog.presentation.auth_routes
@brief The register, login and logout routes.
"""

from flask import Flask, flash, redirect, render_template, url_for
from flask_login import login_user, logout_user
from werkzeug.wrappers import Response

from blog.constants import (
    FLASH_ALREADY_REGISTERED,
    FLASH_UNKNOWN_EMAIL,
    FLASH_WRONG_PASSWORD,
    PAGE_SUBTITLE_LOGIN,
    PAGE_SUBTITLE_REGISTER,
    PAGE_TITLE_LOGIN,
    PAGE_TITLE_REGISTER,
)
from blog.domain.errors import (
    EmailAlreadyRegisteredError,
    InvalidCredentialsError,
    UnknownEmailError,
)
from blog.presentation.auth import LoginUser
from blog.presentation.forms import LoginForm, RegisterForm
from blog.presentation.services import current_use_cases
from blog.presentation.view_models import AuthFormPageViewModel, make_page


def register() -> str | Response:
    """
    @brief Show the sign-up form, or create the account and log in.
    @return The form page, or a redirect to the home page after signing up, or
            to the login page when the email is already registered.
    """
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            user = current_use_cases().register_user.execute(form.to_registration())
        except EmailAlreadyRegisteredError:
            flash(FLASH_ALREADY_REGISTERED)
            return redirect(url_for("login"))
        login_user(LoginUser(user))
        return redirect(url_for("get_all_posts"))
    view = AuthFormPageViewModel(
        page=make_page(PAGE_TITLE_REGISTER, PAGE_SUBTITLE_REGISTER), form=form
    )
    return render_template("register.html", view=view)


def login() -> str | Response:
    """
    @brief Show the login form, or check the credentials and log in.
    @return The form page, or a redirect to the home page after logging in.
    """
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = current_use_cases().authenticate_user.execute(
                form.email.data or "", form.password.data or ""
            )
        except UnknownEmailError:
            flash(FLASH_UNKNOWN_EMAIL)
        except InvalidCredentialsError:
            flash(FLASH_WRONG_PASSWORD)
        else:
            login_user(LoginUser(user))
            return redirect(url_for("get_all_posts"))
    view = AuthFormPageViewModel(
        page=make_page(PAGE_TITLE_LOGIN, PAGE_SUBTITLE_LOGIN), form=form
    )
    return render_template("login.html", view=view)


def logout() -> Response:
    """
    @brief Log the current user out.
    @return A redirect to the home page; the target is fixed, never a request
            parameter, so it cannot be an open redirect.
    """
    logout_user()
    return redirect(url_for("get_all_posts"))


def register_auth_routes(app: Flask) -> None:
    """
    @brief Attach the account routes to an application.
    @param app The application.
    """
    app.add_url_rule("/register", view_func=register, methods=["GET", "POST"])
    app.add_url_rule("/login", view_func=login, methods=["GET", "POST"])
    app.add_url_rule("/logout", view_func=logout)
