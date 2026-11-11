"""
@file
@package tests.integration.test_comments
@brief Commenting, the comment list, avatars and cascade delete.
"""

from flask import Flask
from flask.testing import FlaskClient
from markupsafe import escape

from blog.constants import FLASH_LOGIN_TO_COMMENT
from blog.infrastructure.database import CommentModel, PostModel, UserModel, db
from blog.infrastructure.gravatar import GravatarAvatarProvider
from tests.integration.conftest import MEMBER_NAME, sign_up

COMMENT = {"comment_text": "<p>Nice post</p>"}


def _comments(app: Flask) -> list[CommentModel]:
    """
    @brief Read every stored comment.
    @param app The application.
    @return The rows.
    """
    with app.app_context():
        return list(db.session.scalars(db.select(CommentModel)))


def test_post_page_shows_comment_form_to_everyone(
    app_with_posts: Flask, client: FlaskClient
) -> None:
    """@brief The form has one editor field and the Submit Comment button."""
    html = client.get("/post/1").get_data(as_text=True)
    assert 'name="comment_text"' in html
    assert "Submit Comment" in html


def test_logged_in_user_comment_is_saved_with_author_and_post(
    app_with_posts: Flask, member_client: FlaskClient
) -> None:
    """@brief A comment is stored and the user is sent back to the post."""
    response = member_client.post("/post/2", data=COMMENT)
    assert response.status_code == 302
    assert response.headers["Location"] == "/post/2"
    with app_with_posts.app_context():
        row = db.session.scalars(db.select(CommentModel)).one()
        assert row.text == "<p>Nice post</p>"
        assert row.post_id == 2
        assert row.comment_author.name == MEMBER_NAME


def test_anonymous_comment_redirects_to_login_and_saves_nothing(
    app_with_posts: Flask, client: FlaskClient
) -> None:
    """@brief A visitor is flashed a message and sent to the login page."""
    response = client.post("/post/1", data=COMMENT)
    assert response.status_code == 302
    assert response.headers["Location"] == "/login"
    assert str(escape(FLASH_LOGIN_TO_COMMENT)) in client.get("/login").get_data(
        as_text=True
    )
    assert _comments(app_with_posts) == []


def test_empty_comment_is_not_saved_and_flashes(
    app_with_posts: Flask, member_client: FlaskClient
) -> None:
    """@brief A comment with nothing left after cleaning is dropped."""
    response = member_client.post("/post/1", data={"comment_text": "<p></p>"})
    assert response.headers["Location"] == "/post/1"
    assert "nothing was saved" in member_client.get("/post/1").get_data(as_text=True)
    assert _comments(app_with_posts) == []


def test_invalid_comment_form_shows_page_again(
    app_with_posts: Flask, member_client: FlaskClient
) -> None:
    """@brief A missing comment text shows the form with the message."""
    response = member_client.post("/post/1", data={"comment_text": ""})
    assert response.status_code == 200
    assert "This field is required." in response.get_data(as_text=True)
    assert _comments(app_with_posts) == []


def test_comment_post_for_unknown_post_is_404(member_client: FlaskClient) -> None:
    """@brief Commenting on a missing post gives 404."""
    assert member_client.post("/post/999", data=COMMENT).status_code == 404


def test_comments_are_listed_with_author_name_and_avatar(
    app_with_posts: Flask, member_client: FlaskClient, client: FlaskClient
) -> None:
    """@brief Every visitor sees the comment, its author and the Gravatar image."""
    member_client.post("/post/1", data=COMMENT)
    html = client.get("/post/1").get_data(as_text=True)
    avatar = GravatarAvatarProvider().avatar_url("member@example.com")
    assert "<p>Nice post</p>" in html
    assert MEMBER_NAME in html
    assert f'src="{escape(avatar)}"' in html
    assert f'alt="Avatar of {MEMBER_NAME}"' in html
    assert "Nice post" not in client.get("/post/2").get_data(as_text=True)


def test_script_in_comment_is_stripped(
    app_with_posts: Flask, member_client: FlaskClient
) -> None:
    """@brief Unsafe markup never reaches the page."""
    member_client.post(
        "/post/1", data={"comment_text": "<p>ok</p><script>alert(1)</script>"}
    )
    html = member_client.get("/post/1").get_data(as_text=True)
    assert "<p>ok</p>" in html
    assert "<script>alert(1)" not in html


def test_comment_relationships_work_both_ways(
    app_with_posts: Flask, member_client: FlaskClient
) -> None:
    """@brief user.comments, post.comments and the comment links agree."""
    member_client.post("/post/1", data=COMMENT)
    with app_with_posts.app_context():
        comment = db.session.scalars(db.select(CommentModel)).one()
        member = db.session.get(UserModel, 2)
        post = db.session.get(PostModel, 1)
        assert member is not None
        assert post is not None
        assert comment.comment_author is member
        assert comment.parent_post is post
        assert member.comments == [comment]
        assert post.comments == [comment]


def test_deleting_a_post_deletes_its_comments(
    app_with_posts: Flask, member_client: FlaskClient, admin_client: FlaskClient
) -> None:
    """@brief Comments of a deleted post are removed, others stay."""
    member_client.post("/post/1", data=COMMENT)
    member_client.post("/post/2", data=COMMENT)
    assert admin_client.post("/delete/1").status_code == 302
    remaining = _comments(app_with_posts)
    assert [c.post_id for c in remaining] == [2]


def test_register_stores_lowercase_email_and_login_ignores_case(
    app: Flask, client: FlaskClient
) -> None:
    """@brief Capitals in the email do not make a second account."""
    sign_up(client, " Ann@Example.com ", "Ann")
    client.get("/logout")
    other = app.test_client()
    other.post(
        "/register",
        data={"email": "ANN@example.com", "password": "secret", "name": "Ann"},
    )
    with app.app_context():
        emails = [u.email for u in db.session.scalars(db.select(UserModel))]
    assert emails == ["ann@example.com"]
    login = other.post(
        "/login", data={"email": "ANN@EXAMPLE.com", "password": "secret"}
    )
    assert login.headers["Location"] == "/"


def test_comment_repository_refuses_unsaved_author(app: Flask) -> None:
    """@brief A comment needs an author that is stored."""
    import pytest

    from blog.domain.comment import Comment
    from blog.domain.user import User
    from blog.infrastructure.comment_repository import SqlAlchemyCommentRepository

    comment = Comment(None, "x", User(None, "a@b.c", "h", "A"), 1)
    with app.app_context(), pytest.raises(ValueError, match="author"):
        SqlAlchemyCommentRepository().add(comment)
