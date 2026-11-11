"""
@file
@package blog.infrastructure.html_sanitizer
@brief The HTML sanitizer port backed by bleach.
"""

import bleach

from blog.constants import (
    ALLOWED_HTML_ATTRIBUTES,
    ALLOWED_HTML_PROTOCOLS,
    ALLOWED_HTML_TAGS,
)


class BleachHtmlSanitizer:
    """@brief Keeps only the markup CKEditor produces and drops the rest."""

    def sanitize(self, html: str) -> str:
        """
        @brief Clean a piece of HTML.
        @param html The HTML as submitted.
        @return HTML with disallowed tags removed and only the allowed
                attributes and URL schemes kept.
        """
        attributes = {
            tag: list(names) for tag, names in ALLOWED_HTML_ATTRIBUTES.items()
        }
        return bleach.clean(
            html,
            tags=ALLOWED_HTML_TAGS,
            attributes=attributes,
            protocols=ALLOWED_HTML_PROTOCOLS,
            strip=True,
        )

    def text_of(self, html: str) -> str:
        """
        @brief Read the plain text of a piece of HTML.
        @param html The HTML.
        @return The text with every tag removed.
        """
        return str(bleach.clean(html, tags=set(), strip=True))
