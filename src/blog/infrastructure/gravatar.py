"""
@file
@package blog.infrastructure.gravatar
@brief The avatar provider port backed by Gravatar (no network call is made).
"""

import hashlib
from urllib.parse import urlencode

from blog.constants import (
    GRAVATAR_BASE_URL,
    GRAVATAR_DEFAULT_IMAGE,
    GRAVATAR_RATING,
    GRAVATAR_SIZE,
)
from blog.domain.user import normalise_email


class GravatarAvatarProvider:
    """@brief Builds Gravatar addresses from the SHA-256 hash of an email."""

    def avatar_url(self, email: str) -> str:
        """
        @brief Build the avatar address of an email.
        @param email The email; spaces and letter case do not matter.
        @return The https address of the image.
        """
        digest = hashlib.sha256(normalise_email(email).encode()).hexdigest()
        query = urlencode(
            {"s": GRAVATAR_SIZE, "d": GRAVATAR_DEFAULT_IMAGE, "r": GRAVATAR_RATING}
        )
        return f"{GRAVATAR_BASE_URL}/{digest}?{query}"
