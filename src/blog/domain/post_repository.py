"""
@file
@package blog.domain.post_repository
@brief The port through which the rules store and read posts.
"""

from typing import Protocol

from blog.domain.post import BlogPost


class PostRepository(Protocol):
    """@brief Storage of posts, implemented by an outer layer."""

    def list_all(self) -> list[BlogPost]:
        """
        @brief Read every post.
        @return The posts, oldest first.
        """
        ...

    def get(self, post_id: int) -> BlogPost:
        """
        @brief Read one post.
        @param post_id The id of the post.
        @return The post.
        @throws PostNotFoundError When no post has the id.
        """
        ...

    def add(self, post: BlogPost) -> BlogPost:
        """
        @brief Store a new post.
        @param post The post to store; its id is ignored.
        @return The stored post, with its new id.
        """
        ...

    def update(self, post: BlogPost) -> BlogPost:
        """
        @brief Replace a stored post.
        @param post The new content; its id selects the post.
        @return The stored post.
        @throws PostNotFoundError When no post has the id.
        """
        ...

    def delete(self, post_id: int) -> None:
        """
        @brief Remove a post.
        @param post_id The id of the post.
        @throws PostNotFoundError When no post has the id.
        """
        ...
