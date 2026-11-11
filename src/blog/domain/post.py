"""
@file
@package blog.domain.post
@brief The blog post entity.
"""

from dataclasses import dataclass
from datetime import date

from blog.constants import DATE_FORMAT_MONTH_PATTERN


@dataclass(frozen=True, slots=True)
class BlogPost:
    """@brief One blog post; ``id`` is None until the repository stores it."""

    id: int | None
    title: str
    subtitle: str
    date: str
    body: str
    author: str
    img_url: str


def format_post_date(day: date) -> str:
    """
    @brief Write a day the way posts show it, for example "November 11, 2026".
    @param day The day to write.
    @return The text, with no zero padding on the day of the month.
    """
    month = day.strftime(DATE_FORMAT_MONTH_PATTERN)
    return f"{month} {day.day}, {day.year}"
