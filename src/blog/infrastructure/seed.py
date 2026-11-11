"""
@file
@package blog.infrastructure.seed
@brief Example posts for a new database.
"""

from blog.constants import SEED_POSTS
from blog.domain.post import BlogPost
from blog.domain.post_repository import PostRepository


def seed_posts_if_empty(repository: PostRepository) -> int:
    """
    @brief Insert the example posts when no post exists.
    @param repository Where posts are stored.
    @return How many posts were inserted.
    """
    if repository.list_all():
        return 0
    for item in SEED_POSTS:
        repository.add(BlogPost(id=None, **item))
    return len(SEED_POSTS)
