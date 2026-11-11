"""
@file
@package blog.application.ports
@brief Ports for things outside the business, such as the clock.
"""

from datetime import date
from typing import Protocol


class HtmlSanitizer(Protocol):
    """@brief Removes unsafe markup from HTML written by a user."""

    def sanitize(self, html: str) -> str:
        """
        @brief Clean a piece of HTML.
        @param html The HTML as submitted.
        @return HTML that keeps only the allowed markup.
        """
        ...

    def text_of(self, html: str) -> str:
        """
        @brief Read the plain text of a piece of HTML.
        @param html The HTML.
        @return The text with every tag removed.
        """
        ...


class AvatarProvider(Protocol):
    """@brief Gives the avatar image address of a person."""

    def avatar_url(self, email: str) -> str:
        """
        @brief Build the avatar address of an email.
        @param email The email.
        @return The address of the image.
        """
        ...


class PasswordHasher(Protocol):
    """@brief Turns passwords into salted hashes and checks them."""

    def hash(self, password: str) -> str:
        """
        @brief Make a salted hash of a password.
        @param password The plain password.
        @return The hash, which is safe to store.
        """
        ...

    def verify(self, password_hash: str, password: str) -> bool:
        """
        @brief Check a password against a stored hash.
        @param password_hash The stored hash.
        @param password The plain password to check.
        @return True when they match.
        """
        ...


class Clock(Protocol):
    """@brief Tells today's date."""

    def today(self) -> date:
        """
        @brief Read today's date.
        @return Today.
        """
        ...
