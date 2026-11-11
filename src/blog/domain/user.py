"""
@file
@package blog.domain.user
@brief The user entity.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class User:
    """@brief A registered user; ``id`` is None until the repository stores it."""

    id: int | None
    email: str
    password_hash: str
    name: str
