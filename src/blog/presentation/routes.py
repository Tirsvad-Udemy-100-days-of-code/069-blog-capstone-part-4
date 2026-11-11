"""
@file
@package blog.presentation.routes
@brief Route functions: each calls a use case and renders a view model.
"""

from typing import cast

from flask import Flask, redirect, render_template, url_for
from werkzeug.wrappers import Response

from blog.constants import (
    ABOUT_HEADING,
    ABOUT_PARAGRAPHS,
    ABOUT_SUBHEADING,
    APP_NAME,
    APP_SUBHEADING,
    CONTACT_HEADING,
    CONTACT_SUBHEADING,
    CONTACT_TEXT,
    PAGE_TITLE_EDIT_POST,
    PAGE_TITLE_FORBIDDEN,
    PAGE_TITLE_NEW_POST,
    PAGE_TITLE_NOT_FOUND,
)
from blog.domain.errors import PostNotFoundError
from blog.domain.user import User
from blog.presentation.auth_routes import register_auth_routes
from blog.presentation.authorisation import (
    admin_only,
    current_domain_user,
    current_user_is_admin,
)
from blog.presentation.forms import PostForm
from blog.presentation.services import current_use_cases
from blog.presentation.view_models import (
    FormPageViewModel,
    HomeViewModel,
    PostPageViewModel,
    TextPageViewModel,
    make_page,
    to_post_view_model,
)


def get_all_posts() -> str:
    """
    @brief Show the home page with a preview of every post.
    @return The page.
    """
    posts = [
        to_post_view_model(post) for post in current_use_cases().list_posts.execute()
    ]
    view = HomeViewModel(
        page=make_page(APP_NAME, APP_SUBHEADING),
        posts=posts,
        is_admin=current_user_is_admin(),
    )
    return render_template("index.html", view=view)


def show_post(post_id: int) -> str:
    """
    @brief Show one post.
    @param post_id The id of the post.
    @return The page; a 404 when the post does not exist.
    """
    post = to_post_view_model(current_use_cases().get_post.execute(post_id))
    view = PostPageViewModel(
        site_name=APP_NAME, post=post, is_admin=current_user_is_admin()
    )
    return render_template("post.html", view=view)


@admin_only
def add_new_post() -> str | Response:
    """
    @brief Show the empty post form, or store the submitted post.
    @return The form page, or a redirect to the home page after saving. Only
            the admin may call it; the post is written by the admin.
    """
    form = PostForm()
    if form.validate_on_submit():
        # admin_only guarantees a logged in user.
        author = cast(User, current_domain_user())
        current_use_cases().create_post.execute(form.to_content(), author)
        return redirect(url_for("get_all_posts"))
    view = FormPageViewModel(
        page=make_page(PAGE_TITLE_NEW_POST, ""), form=form, post_id=None
    )
    return render_template("make-post.html", view=view)


@admin_only
def edit_post(post_id: int) -> str | Response:
    """
    @brief Show the form filled with a post, or store the changes.
    @param post_id The id of the post.
    @return The form page, or a redirect to the post after saving; a 404 when
            the post does not exist.
    """
    use_cases = current_use_cases()
    post = to_post_view_model(use_cases.get_post.execute(post_id))
    form = PostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        body=post.body,
    )
    if form.validate_on_submit():
        use_cases.edit_post.execute(post_id, form.to_content())
        return redirect(url_for("show_post", post_id=post_id))
    view = FormPageViewModel(
        page=make_page(PAGE_TITLE_EDIT_POST, post.title), form=form, post_id=post_id
    )
    return render_template("make-post.html", view=view)


@admin_only
def delete_post(post_id: int) -> Response:
    """
    @brief Remove a post.
    @param post_id The id of the post.
    @return A redirect to the home page; a 404 when the post does not exist.
    """
    current_use_cases().delete_post.execute(post_id)
    return redirect(url_for("get_all_posts"))


def about() -> str:
    """
    @brief Show the about page.
    @return The page.
    """
    view = TextPageViewModel(
        page=make_page(ABOUT_HEADING, ABOUT_SUBHEADING),
        paragraphs=ABOUT_PARAGRAPHS,
    )
    return render_template("about.html", view=view)


def contact() -> str:
    """
    @brief Show the contact page.
    @return The page.
    """
    view = TextPageViewModel(
        page=make_page(CONTACT_HEADING, CONTACT_SUBHEADING),
        paragraphs=(CONTACT_TEXT,),
    )
    return render_template("contact.html", view=view)


def handle_post_not_found(_error: PostNotFoundError) -> tuple[str, int]:
    """
    @brief Turn a missing post into the 404 page.
    @param _error The error raised by a use case.
    @return The page and the status code.
    """
    return handle_page_not_found(None)


def handle_forbidden(_error: Exception) -> tuple[str, int]:
    """
    @brief Render the 403 page.
    @param _error The error, not shown to the visitor.
    @return The page and the status code.
    """
    view = TextPageViewModel(page=make_page(PAGE_TITLE_FORBIDDEN, ""), paragraphs=())
    return render_template("403.html", view=view), 403


def handle_page_not_found(_error: Exception | None) -> tuple[str, int]:
    """
    @brief Render the 404 page.
    @param _error The error, not shown to the visitor.
    @return The page and the status code.
    """
    view = TextPageViewModel(page=make_page(PAGE_TITLE_NOT_FOUND, ""), paragraphs=())
    return render_template("404.html", view=view), 404


def register_routes(app: Flask) -> None:
    """
    @brief Attach the routes and error pages to an application.
    @param app The application.
    """
    app.add_url_rule("/", view_func=get_all_posts)
    app.add_url_rule("/post/<int:post_id>", view_func=show_post)
    app.add_url_rule("/new-post", view_func=add_new_post, methods=["GET", "POST"])
    app.add_url_rule(
        "/edit-post/<int:post_id>", view_func=edit_post, methods=["GET", "POST"]
    )
    app.add_url_rule("/delete/<int:post_id>", view_func=delete_post, methods=["POST"])
    app.add_url_rule("/about", view_func=about)
    app.add_url_rule("/contact", view_func=contact)
    register_auth_routes(app)
    app.register_error_handler(PostNotFoundError, handle_post_not_found)
    app.register_error_handler(403, handle_forbidden)
    app.register_error_handler(404, handle_page_not_found)
