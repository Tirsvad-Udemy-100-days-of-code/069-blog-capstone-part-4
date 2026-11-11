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


class Clock(Protocol):
    """@brief Tells today's date."""

    def today(self) -> date:
        """
        @brief Read today's date.
        @return Today.
        """
        ...
