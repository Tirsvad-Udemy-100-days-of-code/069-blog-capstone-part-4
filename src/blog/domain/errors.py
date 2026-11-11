"""
@file
@package blog.domain.errors
@brief Errors raised by the business rules.
"""


class PostNotFoundError(LookupError):
    """@brief Raised when no post has the requested id."""

    def __init__(self, post_id: int | None) -> None:
        """
        @brief Create the error for one post id.
        @param post_id The id that was not found (None for an unsaved post).
        """
        super().__init__(f"No post with id {post_id}")
        self.post_id = post_id
