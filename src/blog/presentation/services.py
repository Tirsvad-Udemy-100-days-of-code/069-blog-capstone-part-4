"""
@file
@package blog.presentation.services
@brief The use cases that the routes call, built once by the composition root.
"""

from dataclasses import dataclass
from typing import cast

from flask import current_app

from blog.application.comment_use_cases import AddComment, ListComments
from blog.application.use_cases import (
    CreatePost,
    DeletePost,
    EditPost,
    GetPost,
    ListPosts,
)
from blog.application.user_use_cases import AuthenticateUser, GetUser, RegisterUser

USE_CASES_KEY = "blog_use_cases"
"""@brief Key under which the composition root stores the use cases."""


@dataclass(frozen=True, slots=True)
class UseCases:
    """@brief The use cases of the blog."""

    list_posts: ListPosts
    get_post: GetPost
    create_post: CreatePost
    edit_post: EditPost
    delete_post: DeletePost
    register_user: RegisterUser
    authenticate_user: AuthenticateUser
    get_user: GetUser
    add_comment: AddComment
    list_comments: ListComments


def current_use_cases() -> UseCases:
    """
    @brief Read the use cases of the running application.
    @return The use cases.
    """
    return cast(UseCases, current_app.extensions[USE_CASES_KEY])
