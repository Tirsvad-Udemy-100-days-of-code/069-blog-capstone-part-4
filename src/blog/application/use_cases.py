"""
@file
@package blog.application.use_cases
@brief The things a user can do with posts.
"""

from dataclasses import replace

from blog.application.dto import PostContent
from blog.application.ports import Clock, HtmlSanitizer
from blog.domain.post import BlogPost, format_post_date
from blog.domain.post_repository import PostRepository


class ListPosts:
    """@brief Read every post."""

    def __init__(self, repository: PostRepository) -> None:
        """
        @brief Create the use case.
        @param repository Where posts are stored.
        """
        self._repository = repository

    def execute(self) -> list[BlogPost]:
        """
        @brief Run the use case.
        @return All posts.
        """
        return self._repository.list_all()


class GetPost:
    """@brief Read one post."""

    def __init__(self, repository: PostRepository) -> None:
        """
        @brief Create the use case.
        @param repository Where posts are stored.
        """
        self._repository = repository

    def execute(self, post_id: int) -> BlogPost:
        """
        @brief Run the use case.
        @param post_id The id of the post.
        @return The post.
        @throws PostNotFoundError When no post has the id.
        """
        return self._repository.get(post_id)


class CreatePost:
    """@brief Store a new post dated today."""

    def __init__(
        self,
        repository: PostRepository,
        clock: Clock,
        sanitizer: HtmlSanitizer,
    ) -> None:
        """
        @brief Create the use case.
        @param repository Where posts are stored.
        @param clock Source of today's date.
        @param sanitizer Cleans the body before it is stored.
        """
        self._repository = repository
        self._clock = clock
        self._sanitizer = sanitizer

    def execute(self, content: PostContent) -> BlogPost:
        """
        @brief Run the use case.
        @param content What the author wrote.
        @return The stored post.
        """
        post = BlogPost(
            id=None,
            title=content.title,
            subtitle=content.subtitle,
            date=format_post_date(self._clock.today()),
            body=self._sanitizer.sanitize(content.body),
            author=content.author,
            img_url=content.img_url,
        )
        return self._repository.add(post)


class EditPost:
    """@brief Change what the author wrote; the date stays."""

    def __init__(self, repository: PostRepository, sanitizer: HtmlSanitizer) -> None:
        """
        @brief Create the use case.
        @param repository Where posts are stored.
        @param sanitizer Cleans the body before it is stored.
        """
        self._repository = repository
        self._sanitizer = sanitizer

    def execute(self, post_id: int, content: PostContent) -> BlogPost:
        """
        @brief Run the use case.
        @param post_id The id of the post.
        @param content The new text.
        @return The stored post.
        @throws PostNotFoundError When no post has the id.
        """
        existing = self._repository.get(post_id)
        changed = replace(
            existing,
            title=content.title,
            subtitle=content.subtitle,
            img_url=content.img_url,
            author=content.author,
            body=self._sanitizer.sanitize(content.body),
        )
        return self._repository.update(changed)


class DeletePost:
    """@brief Remove a post."""

    def __init__(self, repository: PostRepository) -> None:
        """
        @brief Create the use case.
        @param repository Where posts are stored.
        """
        self._repository = repository

    def execute(self, post_id: int) -> None:
        """
        @brief Run the use case.
        @param post_id The id of the post.
        @throws PostNotFoundError When no post has the id.
        """
        self._repository.delete(post_id)
