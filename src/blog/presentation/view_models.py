"""
@file
@package blog.presentation.view_models
@brief Plain objects that hand the templates what they show.
"""

from dataclasses import dataclass

from flask_wtf import FlaskForm

from blog.constants import APP_NAME
from blog.domain.post import BlogPost
from blog.presentation.forms import PostForm


@dataclass(frozen=True, slots=True)
class PostViewModel:
    """@brief One post as a template shows it."""

    id: int
    title: str
    subtitle: str
    date: str
    body: str
    author_name: str
    img_url: str


@dataclass(frozen=True, slots=True)
class PageViewModel:
    """@brief What every page needs."""

    site_name: str
    heading: str
    subheading: str


@dataclass(frozen=True, slots=True)
class HomeViewModel:
    """@brief The home page: a heading and the post previews."""

    page: PageViewModel
    posts: list[PostViewModel]
    is_admin: bool


@dataclass(frozen=True, slots=True)
class PostPageViewModel:
    """@brief The page of one post."""

    site_name: str
    post: PostViewModel
    is_admin: bool


@dataclass(frozen=True, slots=True)
class TextPageViewModel:
    """@brief A page made of a heading and paragraphs (about, contact)."""

    page: PageViewModel
    paragraphs: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class FormPageViewModel:
    """@brief A page that holds the post form."""

    page: PageViewModel
    form: PostForm
    post_id: int | None


@dataclass(frozen=True, slots=True)
class AuthFormPageViewModel:
    """@brief A page that holds the register or login form."""

    page: PageViewModel
    form: FlaskForm


def to_post_view_model(post: BlogPost) -> PostViewModel:
    """
    @brief Map a stored post to its view model.
    @param post The post; it must have an id.
    @return The view model.
    """
    if post.id is None:
        raise ValueError("A stored post has an id")
    return PostViewModel(
        id=post.id,
        title=post.title,
        subtitle=post.subtitle,
        date=post.date,
        body=post.body,
        author_name=post.author.name,
        img_url=post.img_url,
    )


def make_page(heading: str, subheading: str) -> PageViewModel:
    """
    @brief Build the page header data with the site name.
    @param heading Large heading.
    @param subheading Line below the heading.
    @return The view model.
    """
    return PageViewModel(site_name=APP_NAME, heading=heading, subheading=subheading)
