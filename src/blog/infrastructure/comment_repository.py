"""
@file
@package blog.infrastructure.comment_repository
@brief SQLAlchemy implementation of the comment repository port.
"""

from sqlalchemy import select

from blog.domain.comment import Comment
from blog.infrastructure.database import CommentModel, db
from blog.infrastructure.user_repository import user_to_domain


def _to_domain(row: CommentModel) -> Comment:
    """
    @brief Map a table row to the domain entity.
    @param row The row.
    @return The entity.
    """
    return Comment(
        id=row.id,
        text=row.text,
        author=user_to_domain(row.comment_author),
        post_id=row.post_id,
    )


class SqlAlchemyCommentRepository:
    """@brief Stores comments through the Flask-SQLAlchemy session."""

    def add(self, comment: Comment) -> Comment:
        """
        @brief Store a new comment.
        @param comment The comment to store; its id is ignored.
        @return The stored comment, with its new id.
        @throws ValueError When the author is not stored.
        """
        if comment.author.id is None:
            raise ValueError("A comment needs a stored author")
        row = CommentModel(
            text=comment.text, author_id=comment.author.id, post_id=comment.post_id
        )
        db.session.add(row)
        db.session.commit()
        return _to_domain(row)

    def list_for_post(self, post_id: int) -> list[Comment]:
        """
        @brief Read the comments of one post.
        @param post_id The id of the post.
        @return The comments, oldest first.
        """
        rows = db.session.scalars(
            select(CommentModel)
            .where(CommentModel.post_id == post_id)
            .order_by(CommentModel.id)
        )
        return [_to_domain(row) for row in rows]
