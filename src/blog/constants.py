"""
@file
@package blog.constants
@brief Every constant of the project, defined once.
"""

from collections.abc import Mapping
from typing import Final

APP_NAME: Final[str] = "Clean Blog"
"""@brief Name shown in the page title, navigation bar and footer."""

APP_SUBHEADING: Final[str] = "A Flask blog from 100 Days of Code, Day 69"
"""@brief Sub heading on the home page."""

DEFAULT_HOST: Final[str] = "127.0.0.1"
"""@brief Address the development server binds to."""

DEFAULT_PORT: Final[int] = 5002
"""@brief Port the development server listens on."""

DATABASE_FILE_NAME: Final[str] = "blog.db"
"""@brief SQLite file name, created in the instance folder."""

INSTANCE_DIR_NAME: Final[str] = "instance"
"""@brief Folder (below the working directory) that holds local data."""

SECRET_KEY_ENV_VAR: Final[str] = "BLOG_SECRET_KEY"  # noqa: S105
"""@brief Environment variable that carries the session and CSRF secret."""

TESTING_DATABASE_URI: Final[str] = "sqlite:///:memory:"
"""@brief Database used by the testing configuration."""

TESTING_SECRET_KEY: Final[str] = "testing-only-not-a-secret"  # noqa: S105
"""@brief Fixed key for tests, so the testing configuration is repeatable."""

DATE_FORMAT_MONTH_PATTERN: Final[str] = "%B"
"""@brief strftime pattern for the month name used in post dates."""

TITLE_MAX_LENGTH: Final[int] = 250
"""@brief Longest allowed post title."""

SUBTITLE_MAX_LENGTH: Final[int] = 250
"""@brief Longest allowed post subtitle."""

DATE_MAX_LENGTH: Final[int] = 250
"""@brief Longest stored post date text."""

AUTHOR_MAX_LENGTH: Final[int] = 250
"""@brief Longest allowed author name."""

IMG_URL_MAX_LENGTH: Final[int] = 500
"""@brief Longest allowed image address."""

IMG_URL_PATTERN: Final[str] = r"^(https?://|/)\S+$"
"""@brief An image address is an http(s) URL or a path on this site."""

DEFAULT_POST_IMAGE_URL: Final[str] = "/static/assets/img/post-bg.jpg"
"""@brief Header image of the seeded posts."""

LABEL_TITLE: Final[str] = "Blog Post Title"
"""@brief Label of the title field."""

LABEL_SUBTITLE: Final[str] = "Subtitle"
"""@brief Label of the subtitle field."""

LABEL_AUTHOR: Final[str] = "Your Name"
"""@brief Label of the author field."""

LABEL_IMG_URL: Final[str] = "Blog Image URL"
"""@brief Label of the image address field."""

LABEL_BODY: Final[str] = "Blog Content"
"""@brief Label of the body field."""

LABEL_SUBMIT: Final[str] = "Submit Post"
"""@brief Label of the submit button."""

MESSAGE_REQUIRED: Final[str] = "This field is required."
"""@brief Validation message for an empty required field."""

MESSAGE_IMG_URL_INVALID: Final[str] = "Enter an http(s) address or a path."
"""@brief Validation message for a malformed image address."""

ALLOWED_HTML_TAGS: Final[frozenset[str]] = frozenset(
    {
        "p",
        "br",
        "strong",
        "em",
        "u",
        "s",
        "a",
        "ul",
        "ol",
        "li",
        "blockquote",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "img",
        "code",
        "pre",
    }
)
"""@brief HTML tags that a post body may keep; the CKEditor output set."""

ALLOWED_HTML_ATTRIBUTES: Final[Mapping[str, frozenset[str]]] = {
    "a": frozenset({"href", "title"}),
    "img": frozenset({"src", "alt"}),
}
"""@brief Attributes a post body may keep, per tag."""

ALLOWED_HTML_PROTOCOLS: Final[frozenset[str]] = frozenset({"http", "https", "mailto"})
"""@brief URL schemes a post body link or image may use."""

PAGE_TITLE_NEW_POST: Final[str] = "New Post"
"""@brief Heading of the create page."""

PAGE_TITLE_EDIT_POST: Final[str] = "Edit Post"
"""@brief Heading of the edit page."""

PAGE_TITLE_NOT_FOUND: Final[str] = "Post not found"
"""@brief Heading of the 404 page."""

ABOUT_HEADING: Final[str] = "About Me"
"""@brief Heading of the about page."""

ABOUT_SUBHEADING: Final[str] = "This is what I do."
"""@brief Sub heading of the about page."""

ABOUT_PARAGRAPHS: Final[tuple[str, ...]] = (
    "I write this blog while following the 100 Days of Code course.",
    "Each post is stored in a SQLite database and shown by a Flask application.",
    "The look is the Clean Blog theme by Start Bootstrap.",
)
"""@brief Paragraphs of the about page."""

CONTACT_HEADING: Final[str] = "Contact Me"
"""@brief Heading of the contact page."""

CONTACT_SUBHEADING: Final[str] = "Have questions? I have answers."
"""@brief Sub heading of the contact page."""

CONTACT_TEXT: Final[str] = (
    "Want to get in touch? Write to the owner of the blog; "
    "the contact form is not connected yet."
)
"""@brief Text of the contact page."""

SEED_POSTS: Final[tuple[Mapping[str, str], ...]] = (
    {
        "title": "Why I keep a blog",
        "subtitle": "Writing things down makes them stick.",
        "date": "November 1, 2026",
        "body": "<p>Explaining a topic in my own words shows what I have "
        "not understood yet.</p>",
        "author": "Example Author",
        "img_url": DEFAULT_POST_IMAGE_URL,
    },
    {
        "title": "Learning Flask in small steps",
        "subtitle": "Routes first, then templates, then a database.",
        "date": "November 5, 2026",
        "body": "<p>A route is a function. A template turns data into a page. "
        "A database keeps the data between runs.</p>",
        "author": "Example Author",
        "img_url": DEFAULT_POST_IMAGE_URL,
    },
    {
        "title": "Keeping the rules apart from the framework",
        "subtitle": "Layers make the code easier to test.",
        "date": "November 9, 2026",
        "body": "<p>When the business rules do not import Flask, they can be "
        "tested without a web server.</p>",
        "author": "Example Author",
        "img_url": DEFAULT_POST_IMAGE_URL,
    },
)
"""@brief Example posts inserted when the table is empty."""
