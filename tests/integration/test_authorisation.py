"""
@file
@package tests.integration.test_authorisation
@brief The admin rule, the 403 page, hidden buttons and the user/post relation.
"""

import pytest
from flask import Flask
from flask.testing import FlaskClient

from blog.domain.user import User
from blog.infrastructure.database import PostModel, UserModel, db
from blog.infrastructure.post_repository import SqlAlchemyPostRepository
from tests.integration.conftest import ADMIN_NAME, MEMBER_NAME, post_form, sign_up

PROTECTED = (
    ("GET", "/new-post"),
    ("POST", "/new-post"),
    ("GET", "/edit-post/1"),
    ("POST", "/edit-post/1"),
    ("POST", "/delete/1"),
)


def _request(client: FlaskClient, method: str, url: str) -> int:
    """
    @brief Send a request with valid form data and return the status.
    @param client The client.
    @param method GET or POST.
    @param url The path.
    @return The HTTP status code.
    """
    if method == "GET":
        return client.get(url).status_code
    return client.post(url, data=post_form("Hacked")).status_code


@pytest.mark.parametrize(("method", "url"), PROTECTED)
def test_anonymous_gets_403(
    app_with_posts: Flask, client: FlaskClient, method: str, url: str
) -> None:
    """@brief A visitor who is not logged in is refused."""
    assert _request(client, method, url) == 403


@pytest.mark.parametrize(("method", "url"), PROTECTED)
def test_member_gets_403_and_posts_stay(
    member_client: FlaskClient, method: str, url: str
) -> None:
    """@brief A logged in user who is not the admin is refused and changes nothing."""
    assert _request(member_client, method, url) == 403
    html = member_client.get("/").get_data(as_text=True)
    assert "First post" in html
    assert "Hacked" not in html


def test_forbidden_page_is_rendered(client: FlaskClient) -> None:
    """@brief The 403 page uses the blog layout."""
    html = client.get("/new-post").get_data(as_text=True)
    assert "Not allowed" in html
    assert "Clean Blog" in html


def test_get_for_unknown_id_is_403_for_member(member_client: FlaskClient) -> None:
    """@brief The admin check comes before the lookup of the post."""
    assert member_client.get("/edit-post/999").status_code == 403


def test_admin_can_create_edit_and_delete(admin_client: FlaskClient) -> None:
    """@brief The admin is not refused on any protected route."""
    assert admin_client.get("/new-post").status_code == 200
    assert admin_client.post("/new-post", data=post_form()).status_code == 302
    assert admin_client.get("/edit-post/1").status_code == 200
    assert admin_client.post("/edit-post/1", data=post_form("Z")).status_code == 302
    assert admin_client.post("/delete/1").status_code == 302


def test_first_registered_user_gets_id_one(
    app: Flask, admin_client: FlaskClient
) -> None:
    """@brief The first user is id 1, the second is id 2."""
    sign_up(app.test_client(), "second@example.com", MEMBER_NAME)
    with app.app_context():
        ids = {u.email: u.id for u in db.session.scalars(db.select(UserModel))}
    assert ids == {"admin@example.com": 1, "second@example.com": 2}


CONTROLS = ("Create New Post", "Edit Post", "Delete Post", ">Edit</a>", "/delete/1")


def test_admin_sees_buttons(app_with_posts: Flask, admin_client: FlaskClient) -> None:
    """@brief The admin sees create, edit and delete on both pages."""
    index = admin_client.get("/").get_data(as_text=True)
    post = admin_client.get("/post/1").get_data(as_text=True)
    assert "Create New Post" in index
    assert ">Edit</a>" in index
    assert 'action="/delete/1"' in index
    assert "Edit Post" in post
    assert "Delete Post" in post


def test_member_and_visitor_do_not_see_buttons(
    member_client: FlaskClient, client: FlaskClient
) -> None:
    """@brief Everyone else sees none of the admin controls."""
    for visitor in (member_client, client):
        for url in ("/", "/post/1"):
            html = visitor.get(url).get_data(as_text=True)
            for control in CONTROLS:
                assert control not in html, (url, control)


def test_author_name_comes_from_the_user(
    app_with_posts: Flask, admin_client: FlaskClient, client: FlaskClient
) -> None:
    """@brief Both pages show the name of the author user."""
    assert f"Posted by {ADMIN_NAME} on" in client.get("/").get_data(as_text=True)
    assert f"Posted by {ADMIN_NAME} on" in client.get("/post/2").get_data(as_text=True)


def test_relationship_works_both_ways(
    app_with_posts: Flask, admin_client: FlaskClient
) -> None:
    """@brief user.posts lists the posts and post.author is the user."""
    with app_with_posts.app_context():
        admin = db.session.get(UserModel, 1)
        assert admin is not None
        assert [p.title for p in admin.posts] == [
            "First post",
            "Second post",
            "Third post",
        ]
        post = db.session.get(PostModel, 1)
        assert post is not None
        assert post.author is admin
        assert post.author_id == 1


def test_repository_maps_author_to_domain_user(
    app_with_posts: Flask, admin_client: FlaskClient
) -> None:
    """@brief A post read from the repository carries its author as a User."""
    with app_with_posts.app_context():
        post = SqlAlchemyPostRepository().get(1)
    assert post.author == User(
        1, "admin@example.com", post.author.password_hash, ADMIN_NAME
    )


def test_repository_refuses_post_with_unsaved_author(app: Flask) -> None:
    """@brief A post needs an author that is stored."""
    from blog.domain.post import BlogPost

    post = BlogPost(None, "t", "s", "d", "b", User(None, "a@b.c", "h", "A"), "/i")
    with app.app_context(), pytest.raises(ValueError, match="author"):
        SqlAlchemyPostRepository().add(post)
