"""
@file
@package blog.application.comment_use_cases
@brief The things a visitor can do about comments.
"""

from blog.application.dto import CommentDetails
from blog.application.ports import AvatarProvider, HtmlSanitizer
from blog.domain.comment import Comment
from blog.domain.comment_repository import CommentRepository
from blog.domain.errors import EmptyCommentError
from blog.domain.user import User


class AddComment:
    """@brief Store a comment, keeping only safe HTML."""

    def __init__(self, repository: CommentRepository, sanitizer: HtmlSanitizer) -> None:
        """
        @brief Create the use case.
        @param repository Where comments are stored.
        @param sanitizer Cleans the text before it is stored.
        """
        self._repository = repository
        self._sanitizer = sanitizer

    def execute(self, text: str, author: User, post_id: int) -> Comment:
        """
        @brief Run the use case.
        @param text The comment as HTML.
        @param author The user who writes it.
        @param post_id The post it belongs to.
        @return The stored comment.
        @throws EmptyCommentError When no text is left after cleaning.
        """
        clean_text = self._sanitizer.sanitize(text).strip()
        if not self._sanitizer.text_of(clean_text).strip():
            raise EmptyCommentError
        comment = Comment(id=None, text=clean_text, author=author, post_id=post_id)
        return self._repository.add(comment)


class ListComments:
    """@brief Read the comments of a post, each with its avatar address."""

    def __init__(self, repository: CommentRepository, avatars: AvatarProvider) -> None:
        """
        @brief Create the use case.
        @param repository Where comments are stored.
        @param avatars Gives the avatar address of an email.
        """
        self._repository = repository
        self._avatars = avatars

    def execute(self, post_id: int) -> list[CommentDetails]:
        """
        @brief Run the use case.
        @param post_id The id of the post.
        @return The comments, oldest first.
        """
        return [
            CommentDetails(
                author_name=comment.author.name,
                text=comment.text,
                avatar_url=self._avatars.avatar_url(comment.author.email),
            )
            for comment in self._repository.list_for_post(post_id)
        ]
