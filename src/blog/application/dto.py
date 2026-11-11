"""
@file
@package blog.application.dto
@brief Plain input types of the use cases.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PostContent:
    """@brief The parts of a post that the author writes; the author is not one."""

    title: str
    subtitle: str
    img_url: str
    body: str


@dataclass(frozen=True, slots=True)
class Registration:
    """@brief What a person enters to sign up."""

    email: str
    password: str
    name: str


@dataclass(frozen=True, slots=True)
class CommentDetails:
    """@brief A comment as the pages show it."""

    author_name: str
    text: str
    avatar_url: str
