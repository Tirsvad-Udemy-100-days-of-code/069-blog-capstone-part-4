"""
@file
@package tests.unit.test_use_cases
@brief Tests of the use cases against a fake repository.
"""

import pytest

from blog.application.dto import PostContent
from blog.application.use_cases import (
    CreatePost,
    DeletePost,
    EditPost,
    GetPost,
    ListPosts,
)
from blog.domain.errors import PostNotFoundError
from blog.infrastructure.html_sanitizer import BleachHtmlSanitizer
from blog.infrastructure.seed import seed_posts_if_empty
from tests.unit.fakes import FixedClock, InMemoryPostRepository

CONTENT = PostContent(
    title="Title", subtitle="Sub", img_url="/img.jpg", author="Ann", body="<p>x</p>"
)


def test_list_posts_returns_empty_list_when_no_posts(
    repository: InMemoryPostRepository,
) -> None:
    """@brief No posts gives an empty list."""
    assert ListPosts(repository).execute() == []


def test_create_post_stores_post_dated_today(
    repository: InMemoryPostRepository, clock: FixedClock
) -> None:
    """@brief A new post gets an id and today's date."""
    post = CreatePost(repository, clock, BleachHtmlSanitizer()).execute(CONTENT)
    assert post.id == 1
    assert post.date == "November 5, 2026"
    assert post.title == "Title"
    assert ListPosts(repository).execute() == [post]


def test_get_post_returns_stored_post(
    repository: InMemoryPostRepository, clock: FixedClock
) -> None:
    """@brief A stored post can be read by id."""
    created = CreatePost(repository, clock, BleachHtmlSanitizer()).execute(CONTENT)
    assert GetPost(repository).execute(1) == created


def test_get_post_raises_when_id_unknown(
    repository: InMemoryPostRepository,
) -> None:
    """@brief An unknown id is refused."""
    with pytest.raises(PostNotFoundError):
        GetPost(repository).execute(99)


def test_edit_post_changes_text_and_keeps_date(
    repository: InMemoryPostRepository, clock: FixedClock
) -> None:
    """@brief Editing replaces the text but not the date or id."""
    CreatePost(repository, clock, BleachHtmlSanitizer()).execute(CONTENT)
    new = PostContent("New", "New sub", "/n.jpg", "Bob", "<p>n</p>")
    edited = EditPost(repository, BleachHtmlSanitizer()).execute(1, new)
    assert (edited.id, edited.date) == (1, "November 5, 2026")
    assert (edited.title, edited.author, edited.body) == ("New", "Bob", "<p>n</p>")
    assert repository.get(1) == edited


def test_edit_post_raises_when_id_unknown(
    repository: InMemoryPostRepository,
) -> None:
    """@brief Editing an unknown post is refused."""
    with pytest.raises(PostNotFoundError):
        EditPost(repository, BleachHtmlSanitizer()).execute(5, CONTENT)


def test_delete_post_removes_post(
    repository: InMemoryPostRepository, clock: FixedClock
) -> None:
    """@brief A deleted post is gone."""
    CreatePost(repository, clock, BleachHtmlSanitizer()).execute(CONTENT)
    DeletePost(repository).execute(1)
    assert ListPosts(repository).execute() == []


def test_delete_post_raises_when_id_unknown(
    repository: InMemoryPostRepository,
) -> None:
    """@brief Deleting an unknown post is refused."""
    with pytest.raises(PostNotFoundError):
        DeletePost(repository).execute(1)


def test_seed_inserts_posts_when_empty(
    repository: InMemoryPostRepository,
) -> None:
    """@brief An empty store receives the three example posts."""
    assert seed_posts_if_empty(repository) == 3
    assert len(repository.list_all()) == 3


def test_seed_does_nothing_when_posts_exist(
    repository: InMemoryPostRepository, clock: FixedClock
) -> None:
    """@brief A store with posts is left alone."""
    CreatePost(repository, clock, BleachHtmlSanitizer()).execute(CONTENT)
    assert seed_posts_if_empty(repository) == 0
    assert len(repository.list_all()) == 1
