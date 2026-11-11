"""
@file
@package tests.unit.test_post_domain
@brief Tests of the domain entity, date format and error.
"""

from dataclasses import FrozenInstanceError
from datetime import date

import pytest

from blog.domain.errors import PostNotFoundError
from blog.domain.post import BlogPost, format_post_date
from blog.domain.user import User, is_admin


def test_format_post_date_has_no_zero_padding() -> None:
    """@brief A single digit day is written without a leading zero."""
    assert format_post_date(date(2026, 11, 5)) == "November 5, 2026"


def test_format_post_date_two_digit_day() -> None:
    """@brief A two digit day is written as it is."""
    assert format_post_date(date(2026, 11, 11)) == "November 11, 2026"


def test_format_post_date_leap_day() -> None:
    """@brief 29 February of a leap year is formatted."""
    assert format_post_date(date(2028, 2, 29)) == "February 29, 2028"


def test_blog_post_is_immutable() -> None:
    """@brief A post cannot be changed after it is made."""
    post = BlogPost(
        None, "t", "s", "d", "<p>b</p>", User(1, "a@b.c", "h", "A"), "/i.jpg"
    )
    with pytest.raises(FrozenInstanceError):
        post.title = "other"  # type: ignore[misc]


def test_post_not_found_error_keeps_id_and_message() -> None:
    """@brief The error names the id that was not found."""
    error = PostNotFoundError(7)
    assert error.post_id == 7
    assert "7" in str(error)
    assert isinstance(error, LookupError)


def test_is_admin_true_for_user_id_one() -> None:
    """@brief The first registered user is the admin."""
    assert is_admin(User(1, "a@b.c", "h", "A"))


def test_is_admin_false_for_other_user_ids() -> None:
    """@brief Any other id is not the admin."""
    assert not is_admin(User(2, "a@b.c", "h", "A"))
    assert not is_admin(User(0, "a@b.c", "h", "A"))


def test_is_admin_false_for_visitor_and_unsaved_user() -> None:
    """@brief A visitor (None) and a user without id are not the admin."""
    assert not is_admin(None)
    assert not is_admin(User(None, "a@b.c", "h", "A"))
