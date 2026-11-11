"""
@file
@package blog.application.dto
@brief Plain input types of the use cases.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PostContent:
    """@brief The parts of a post that an author writes."""

    title: str
    subtitle: str
    img_url: str
    author: str
    body: str
