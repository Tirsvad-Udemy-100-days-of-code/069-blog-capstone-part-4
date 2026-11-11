"""
@file
@package tests.unit.test_comment_use_cases
@brief Tests of the comment use cases, the Gravatar adapter and email handling.
"""

from dataclasses import replace

import pytest

from blog.application.comment_use_cases import AddComment, ListComments
from blog.application.dto import Registration
from blog.application.user_use_cases import AuthenticateUser, RegisterUser
from blog.domain.comment import Comment
from blog.domain.errors import EmailAlreadyRegisteredError, EmptyCommentError
from blog.domain.user import User, normalise_email
from blog.infrastructure.gravatar import GravatarAvatarProvider
from blog.infrastructure.html_sanitizer import BleachHtmlSanitizer
from tests.unit.fakes import InMemoryUserRepository, ReversingPasswordHasher

AUTHOR = User(7, "Ann@Example.com", "hash", "Ann")
KNOWN_HASH = "16c18d336f0b250f0e2d907452ceb9658a74ecdae8bc94864c23122a72cc27a5"


class InMemoryCommentRepository:
    """@brief A list behind the CommentRepository port."""

    def __init__(self) -> None:
        """@brief Create an empty repository."""
        self.comments: list[Comment] = []

    def add(self, comment: Comment) -> Comment:
        """
        @brief Store a comment under a new id.
        @param comment The comment.
        @return The stored comment.
        """
        stored = replace(comment, id=len(self.comments) + 1)
        self.comments.append(stored)
        return stored

    def list_for_post(self, post_id: int) -> list[Comment]:
        """
        @brief Read the comments of a post.
        @param post_id The post id.
        @return The comments.
        """
        return [c for c in self.comments if c.post_id == post_id]


class FakeAvatars:
    """@brief An avatar provider that makes no hash."""

    def avatar_url(self, email: str) -> str:
        """
        @brief Build a fake address.
        @param email The email.
        @return The address.
        """
        return f"https://avatars.test/{email}"


def test_add_comment_stores_comment_with_author_and_post() -> None:
    """@brief A comment is saved with its author and post."""
    repository = InMemoryCommentRepository()
    comment = AddComment(repository, BleachHtmlSanitizer()).execute(
        "<p>Hi</p>", AUTHOR, 3
    )
    assert comment.id == 1
    assert (comment.text, comment.author, comment.post_id) == ("<p>Hi</p>", AUTHOR, 3)


def test_add_comment_sanitizes_html() -> None:
    """@brief A script tag does not survive."""
    repository = InMemoryCommentRepository()
    comment = AddComment(repository, BleachHtmlSanitizer()).execute(
        "<p>Hi</p><script>alert(1)</script>", AUTHOR, 1
    )
    assert "<script" not in comment.text
    assert "<p>Hi</p>" in comment.text


@pytest.mark.parametrize("text", ["", "   ", "<p></p>", "<script></script>"])
def test_add_comment_rejects_empty_text(text: str) -> None:
    """@brief Text with nothing left after cleaning is refused."""
    repository = InMemoryCommentRepository()
    with pytest.raises(EmptyCommentError):
        AddComment(repository, BleachHtmlSanitizer()).execute(text, AUTHOR, 1)
    assert repository.comments == []


def test_list_comments_returns_details_for_one_post() -> None:
    """@brief Only the comments of the post are listed, with name and avatar."""
    repository = InMemoryCommentRepository()
    add = AddComment(repository, BleachHtmlSanitizer())
    add.execute("<p>one</p>", AUTHOR, 1)
    add.execute("<p>other post</p>", AUTHOR, 2)
    details = ListComments(repository, FakeAvatars()).execute(1)
    assert len(details) == 1
    assert details[0].author_name == "Ann"
    assert details[0].text == "<p>one</p>"
    assert details[0].avatar_url == "https://avatars.test/Ann@Example.com"


def test_list_comments_empty_for_post_without_comments() -> None:
    """@brief A post without comments gives an empty list."""
    assert ListComments(InMemoryCommentRepository(), FakeAvatars()).execute(1) == []


def test_gravatar_url_uses_sha256_of_email() -> None:
    """@brief The address holds the known SHA-256 of the email and the options."""
    url = GravatarAvatarProvider().avatar_url("myemail@example.com")
    assert url == (f"https://www.gravatar.com/avatar/{KNOWN_HASH}?s=100&d=retro&r=g")


def test_gravatar_url_trims_and_lowercases_email() -> None:
    """@brief Spaces and capitals give the same address."""
    provider = GravatarAvatarProvider()
    assert provider.avatar_url("  MyEmail@Example.COM ") == provider.avatar_url(
        "myemail@example.com"
    )


def test_normalise_email_trims_and_lowercases() -> None:
    """@brief The stored form of an email."""
    assert normalise_email("  A@X.com ") == "a@x.com"


def test_register_user_treats_emails_with_other_case_as_the_same_account() -> None:
    """@brief A@x.com and a@x.com are one account."""
    repository = InMemoryUserRepository()
    use_case = RegisterUser(repository, ReversingPasswordHasher())
    user = use_case.execute(Registration(" A@x.com ", "pw", "A"))
    assert user.email == "a@x.com"
    with pytest.raises(EmailAlreadyRegisteredError):
        use_case.execute(Registration("a@X.COM", "pw", "B"))


def test_authenticate_user_ignores_case_and_spaces_of_email() -> None:
    """@brief Login works with the email typed in another case."""
    repository = InMemoryUserRepository()
    hasher = ReversingPasswordHasher()
    RegisterUser(repository, hasher).execute(Registration("a@x.com", "pw", "A"))
    user = AuthenticateUser(repository, hasher).execute(" A@X.com ", "pw")
    assert user.email == "a@x.com"
