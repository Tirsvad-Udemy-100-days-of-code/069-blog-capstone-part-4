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

ADMIN_USER_ID: Final[int] = 1
"""@brief Id of the admin: the first registered user."""

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

IMG_URL_MAX_LENGTH: Final[int] = 500
"""@brief Longest allowed image address."""

IMG_URL_PATTERN: Final[str] = r"^(https?://|/)\S+$"
"""@brief An image address is an http(s) URL or a path on this site."""

LABEL_TITLE: Final[str] = "Blog Post Title"
"""@brief Label of the title field."""

LABEL_SUBTITLE: Final[str] = "Subtitle"
"""@brief Label of the subtitle field."""

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

EMAIL_MAX_LENGTH: Final[int] = 250
"""@brief Longest allowed email address."""

NAME_MAX_LENGTH: Final[int] = 250
"""@brief Longest allowed user name."""

PASSWORD_HASH_MAX_LENGTH: Final[int] = 250
"""@brief Room for a stored password hash."""

PASSWORD_HASH_METHOD: Final[str] = "pbkdf2:sha256"  # noqa: S105
"""@brief Werkzeug hash method for passwords."""

PASSWORD_SALT_LENGTH: Final[int] = 8
"""@brief Length of the random salt added to each password."""

LABEL_EMAIL: Final[str] = "Email"
"""@brief Label of the email field."""

LABEL_PASSWORD: Final[str] = "Password"  # noqa: S105
"""@brief Label of the password field."""

LABEL_USER_NAME: Final[str] = "Name"
"""@brief Label of the name field of the register form."""

GRAVATAR_BASE_URL: Final[str] = "https://www.gravatar.com/avatar"
"""@brief Address that serves Gravatar images."""

GRAVATAR_SIZE: Final[int] = 100
"""@brief Side of the avatar image in pixels."""

GRAVATAR_DEFAULT_IMAGE: Final[str] = "retro"
"""@brief Image Gravatar draws when an email has no avatar."""

GRAVATAR_RATING: Final[str] = "g"
"""@brief Highest content rating of the avatar."""

LABEL_COMMENT: Final[str] = "Comment"
"""@brief Label of the comment field."""

LABEL_COMMENT_SUBMIT: Final[str] = "Submit Comment"
"""@brief Label of the comment button."""

FLASH_LOGIN_TO_COMMENT: Final[str] = "You need to login or register to comment."
"""@brief Shown when a visitor who is not logged in submits a comment."""

FLASH_EMPTY_COMMENT: Final[str] = "Your comment is empty, nothing was saved."
"""@brief Shown when a comment has no text left after cleaning."""

LABEL_REGISTER_SUBMIT: Final[str] = "Sign Me Up!"
"""@brief Label of the register button."""

LABEL_LOGIN_SUBMIT: Final[str] = "Let Me In!"
"""@brief Label of the login button."""

MESSAGE_EMAIL_INVALID: Final[str] = "Enter a valid email address."
"""@brief Validation message for a malformed email."""

FLASH_ALREADY_REGISTERED: Final[str] = (
    "You've already signed up with that email, log in instead!"
)
"""@brief Shown when registering with a known email."""

FLASH_UNKNOWN_EMAIL: Final[str] = "That email does not exist, please try again."
"""@brief Shown when logging in with an unknown email."""

FLASH_WRONG_PASSWORD: Final[str] = "Password incorrect, please try again."  # noqa: S105
"""@brief Shown when logging in with a wrong password."""

PAGE_TITLE_REGISTER: Final[str] = "Register"
"""@brief Heading of the register page."""

PAGE_SUBTITLE_REGISTER: Final[str] = "Start contributing to the blog!"
"""@brief Sub heading of the register page."""

PAGE_TITLE_LOGIN: Final[str] = "Log In"
"""@brief Heading of the login page."""

PAGE_SUBTITLE_LOGIN: Final[str] = "Welcome back!"
"""@brief Sub heading of the login page."""

PAGE_TITLE_NEW_POST: Final[str] = "New Post"
"""@brief Heading of the create page."""

PAGE_TITLE_EDIT_POST: Final[str] = "Edit Post"
"""@brief Heading of the edit page."""

PAGE_TITLE_FORBIDDEN: Final[str] = "Not allowed"
"""@brief Heading of the 403 page."""

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
