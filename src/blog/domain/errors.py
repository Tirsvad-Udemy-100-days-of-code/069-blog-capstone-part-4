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


class EmailAlreadyRegisteredError(ValueError):
    """@brief Raised when a user registers with an email that is taken."""

    def __init__(self, email: str) -> None:
        """
        @brief Create the error for one email.
        @param email The email that is already registered.
        """
        super().__init__("That email is already registered")
        self.email = email


class UnknownEmailError(LookupError):
    """@brief Raised at login when no user has the email."""

    def __init__(self, email: str) -> None:
        """
        @brief Create the error for one email.
        @param email The email nobody has registered.
        """
        super().__init__("No user has that email")
        self.email = email


class InvalidCredentialsError(ValueError):
    """@brief Raised at login when the password does not match."""

    def __init__(self) -> None:
        """@brief Create the error."""
        super().__init__("The password is incorrect")
