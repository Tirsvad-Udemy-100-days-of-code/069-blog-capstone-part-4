"""
@file
@package blog.infrastructure.post_repository
@brief SQLAlchemy implementation of the post repository port.
"""

from sqlalchemy import select

from blog.domain.errors import PostNotFoundError
from blog.domain.post import BlogPost
from blog.infrastructure.database import PostModel, db
from blog.infrastructure.user_repository import user_to_domain


def _to_domain(row: PostModel) -> BlogPost:
    """
    @brief Map a table row to the domain entity.
    @param row The row.
    @return The entity.
    """
    return BlogPost(
        id=row.id,
        title=row.title,
        subtitle=row.subtitle,
        date=row.date,
        body=row.body,
        author=user_to_domain(row.author),
        img_url=row.img_url,
    )


def _copy_to_row(post: BlogPost, row: PostModel) -> None:
    """
    @brief Copy the fields of an entity onto a row.
    @param post The entity.
    @param row The row that receives the values.
    """
    row.title = post.title
    row.subtitle = post.subtitle
    row.date = post.date
    row.body = post.body
    if post.author.id is None:
        raise ValueError("A post needs a stored author")
    row.author_id = post.author.id
    row.img_url = post.img_url


def _find_row(post_id: int | None) -> PostModel:
    """
    @brief Load a row or fail.
    @param post_id The id; None never matches.
    @return The row.
    @throws PostNotFoundError When no row has the id.
    """
    row = None if post_id is None else db.session.get(PostModel, post_id)
    if row is None:
        raise PostNotFoundError(post_id)
    return row


class SqlAlchemyPostRepository:
    """@brief Stores posts through the Flask-SQLAlchemy session."""

    def list_all(self) -> list[BlogPost]:
        """
        @brief Read every post.
        @return The posts, oldest first.
        """
        rows = db.session.scalars(select(PostModel).order_by(PostModel.id))
        return [_to_domain(row) for row in rows]

    def get(self, post_id: int) -> BlogPost:
        """
        @brief Read one post.
        @param post_id The id of the post.
        @return The post.
        @throws PostNotFoundError When no post has the id.
        """
        return _to_domain(_find_row(post_id))

    def add(self, post: BlogPost) -> BlogPost:
        """
        @brief Store a new post.
        @param post The post to store; its id is ignored.
        @return The stored post, with its new id.
        """
        row = PostModel()
        _copy_to_row(post, row)
        db.session.add(row)
        db.session.commit()
        return _to_domain(row)

    def update(self, post: BlogPost) -> BlogPost:
        """
        @brief Replace a stored post.
        @param post The new content; its id selects the post.
        @return The stored post.
        @throws PostNotFoundError When no post has the id.
        """
        row = _find_row(post.id)
        _copy_to_row(post, row)
        db.session.commit()
        return _to_domain(row)

    def delete(self, post_id: int) -> None:
        """
        @brief Remove a post.
        @param post_id The id of the post.
        @throws PostNotFoundError When no post has the id.
        """
        db.session.delete(_find_row(post_id))
        db.session.commit()
