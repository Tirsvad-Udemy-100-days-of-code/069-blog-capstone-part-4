"""
@file
@package blog.domain.user_repository
@brief The port through which the rules store and read users.
"""

from typing import Protocol

from blog.domain.user import User


class UserRepository(Protocol):
    """@brief Storage of users, implemented by an outer layer."""

    def add(self, user: User) -> User:
        """
        @brief Store a new user.
        @param user The user to store; its id is ignored.
        @return The stored user, with its new id.
        @throws EmailAlreadyRegisteredError When the email is taken.
        """
        ...

    def get_by_id(self, user_id: int) -> User | None:
        """
        @brief Read a user by id.
        @param user_id The id.
        @return The user, or None when there is none.
        """
        ...

    def get_by_email(self, email: str) -> User | None:
        """
        @brief Read a user by email.
        @param email The email.
        @return The user, or None when there is none.
        """
        ...
