"""
@file
@package blog.domain.user
@brief The user entity.
"""

from dataclasses import dataclass

from blog.constants import ADMIN_USER_ID


@dataclass(frozen=True, slots=True)
class User:
    """@brief A registered user; ``id`` is None until the repository stores it."""

    id: int | None
    email: str
    password_hash: str
    name: str


def is_admin(user: User | None) -> bool:
    """
    @brief Tell whether a user is the admin (the first registered user).
    @param user The user, or None for a visitor who is not logged in.
    @return True only for the admin.
    """
    return user is not None and user.id == ADMIN_USER_ID
