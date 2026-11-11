"""
@file
@package blog.domain.comment
@brief The comment entity.
"""

from dataclasses import dataclass

from blog.domain.user import User


@dataclass(frozen=True, slots=True)
class Comment:
    """@brief A comment on a post; ``id`` is None until it is stored."""

    id: int | None
    text: str
    author: User
    post_id: int
