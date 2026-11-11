"""
@file
@package blog.domain.comment_repository
@brief The port through which the rules store and read comments.
"""

from typing import Protocol

from blog.domain.comment import Comment


class CommentRepository(Protocol):
    """@brief Storage of comments, implemented by an outer layer."""

    def add(self, comment: Comment) -> Comment:
        """
        @brief Store a new comment.
        @param comment The comment to store; its id is ignored.
        @return The stored comment, with its new id.
        """
        ...

    def list_for_post(self, post_id: int) -> list[Comment]:
        """
        @brief Read the comments of one post.
        @param post_id The id of the post.
        @return The comments, oldest first.
        """
        ...
