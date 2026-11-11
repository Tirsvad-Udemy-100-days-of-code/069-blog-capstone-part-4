"""
@file
@package tests.unit.fakes
@brief Fakes of the ports, shared by the unit tests.
"""

from dataclasses import replace
from datetime import date

from blog.domain.errors import EmailAlreadyRegisteredError, PostNotFoundError
from blog.domain.post import BlogPost
from blog.domain.user import User


class InMemoryUserRepository:
    """@brief A dictionary behind the UserRepository port."""

    def __init__(self) -> None:
        """@brief Create an empty repository."""
        self.users: dict[int, User] = {}

    def add(self, user: User) -> User:
        """
        @brief Store a user under a new id.
        @param user The user.
        @return The stored user.
        """
        if self.get_by_email(user.email) is not None:
            raise EmailAlreadyRegisteredError(user.email)
        new_id = len(self.users) + 1
        stored = replace(user, id=new_id)
        self.users[new_id] = stored
        return stored

    def get_by_id(self, user_id: int) -> User | None:
        """
        @brief Read a user by id.
        @param user_id The id.
        @return The user or None.
        """
        return self.users.get(user_id)

    def get_by_email(self, email: str) -> User | None:
        """
        @brief Read a user by email.
        @param email The email.
        @return The user or None.
        """
        return next((u for u in self.users.values() if u.email == email), None)


class ReversingPasswordHasher:
    """@brief A fake hasher: the hash is the reversed password with a prefix."""

    def hash(self, password: str) -> str:
        """
        @brief Make a fake hash.
        @param password The plain password.
        @return The fake hash.
        """
        return "fake$" + password[::-1]

    def verify(self, password_hash: str, password: str) -> bool:
        """
        @brief Check a password against a fake hash.
        @param password_hash The hash.
        @param password The plain password.
        @return True when they match.
        """
        return password_hash == self.hash(password)


class InMemoryPostRepository:
    """@brief A dictionary behind the PostRepository port."""

    def __init__(self) -> None:
        """@brief Create an empty repository."""
        self.posts: dict[int, BlogPost] = {}
        self._next_id = 1

    def list_all(self) -> list[BlogPost]:
        """
        @brief Read every post.
        @return The posts in id order.
        """
        return [self.posts[key] for key in sorted(self.posts)]

    def get(self, post_id: int) -> BlogPost:
        """
        @brief Read one post.
        @param post_id The id.
        @return The post.
        """
        if post_id not in self.posts:
            raise PostNotFoundError(post_id)
        return self.posts[post_id]

    def add(self, post: BlogPost) -> BlogPost:
        """
        @brief Store a post under a new id.
        @param post The post.
        @return The stored post.
        """
        stored = replace(post, id=self._next_id)
        self.posts[self._next_id] = stored
        self._next_id += 1
        return stored

    def update(self, post: BlogPost) -> BlogPost:
        """
        @brief Replace a post.
        @param post The new content.
        @return The stored post.
        """
        if post.id is None or post.id not in self.posts:
            raise PostNotFoundError(post.id)
        self.posts[post.id] = post
        return post

    def delete(self, post_id: int) -> None:
        """
        @brief Remove a post.
        @param post_id The id.
        """
        if post_id not in self.posts:
            raise PostNotFoundError(post_id)
        del self.posts[post_id]


class FixedClock:
    """@brief A clock that always tells the same day."""

    def __init__(self, day: date) -> None:
        """
        @brief Create the clock.
        @param day The day it reports.
        """
        self._day = day

    def today(self) -> date:
        """
        @brief Read the fixed day.
        @return The day.
        """
        return self._day
