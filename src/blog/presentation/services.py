"""
@file
@package blog.presentation.services
@brief The use cases that the routes call, built once by the composition root.
"""

from dataclasses import dataclass

from blog.application.use_cases import (
    CreatePost,
    DeletePost,
    EditPost,
    GetPost,
    ListPosts,
)


@dataclass(frozen=True, slots=True)
class UseCases:
    """@brief The use cases of the blog."""

    list_posts: ListPosts
    get_post: GetPost
    create_post: CreatePost
    edit_post: EditPost
    delete_post: DeletePost
