"""
@file
@package blog.presentation.forms
@brief The post form.
"""

from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp

from blog.application.dto import PostContent, Registration
from blog.constants import (
    EMAIL_MAX_LENGTH,
    IMG_URL_MAX_LENGTH,
    IMG_URL_PATTERN,
    LABEL_BODY,
    LABEL_EMAIL,
    LABEL_IMG_URL,
    LABEL_LOGIN_SUBMIT,
    LABEL_PASSWORD,
    LABEL_REGISTER_SUBMIT,
    LABEL_SUBMIT,
    LABEL_SUBTITLE,
    LABEL_TITLE,
    LABEL_USER_NAME,
    MESSAGE_EMAIL_INVALID,
    MESSAGE_IMG_URL_INVALID,
    MESSAGE_REQUIRED,
    NAME_MAX_LENGTH,
    SUBTITLE_MAX_LENGTH,
    TITLE_MAX_LENGTH,
)


class PostForm(FlaskForm):  # type: ignore[misc]
    """@brief Form used to write and to change a post."""

    title = StringField(
        LABEL_TITLE,
        validators=[DataRequired(MESSAGE_REQUIRED), Length(max=TITLE_MAX_LENGTH)],
    )
    subtitle = StringField(
        LABEL_SUBTITLE,
        validators=[DataRequired(MESSAGE_REQUIRED), Length(max=SUBTITLE_MAX_LENGTH)],
    )
    img_url = StringField(
        LABEL_IMG_URL,
        validators=[
            DataRequired(MESSAGE_REQUIRED),
            Length(max=IMG_URL_MAX_LENGTH),
            Regexp(IMG_URL_PATTERN, message=MESSAGE_IMG_URL_INVALID),
        ],
    )
    body = CKEditorField(LABEL_BODY, validators=[DataRequired(MESSAGE_REQUIRED)])
    submit = SubmitField(LABEL_SUBMIT)

    def to_content(self) -> PostContent:
        """
        @brief Read the validated fields as use case input.
        @return What the author wrote (the author is the logged in user).
        """
        return PostContent(
            title=self.title.data or "",
            subtitle=self.subtitle.data or "",
            img_url=self.img_url.data or "",
            body=self.body.data or "",
        )


class RegisterForm(FlaskForm):  # type: ignore[misc]
    """@brief Form used to sign up."""

    email = StringField(
        LABEL_EMAIL,
        validators=[
            DataRequired(MESSAGE_REQUIRED),
            Email(MESSAGE_EMAIL_INVALID),
            Length(max=EMAIL_MAX_LENGTH),
        ],
    )
    password = PasswordField(
        LABEL_PASSWORD, validators=[DataRequired(MESSAGE_REQUIRED)]
    )
    name = StringField(
        LABEL_USER_NAME,
        validators=[DataRequired(MESSAGE_REQUIRED), Length(max=NAME_MAX_LENGTH)],
    )
    submit = SubmitField(LABEL_REGISTER_SUBMIT)

    def to_registration(self) -> Registration:
        """
        @brief Read the validated fields as use case input.
        @return What the person entered.
        """
        return Registration(
            email=self.email.data or "",
            password=self.password.data or "",
            name=self.name.data or "",
        )


class LoginForm(FlaskForm):  # type: ignore[misc]
    """@brief Form used to log in."""

    email = StringField(
        LABEL_EMAIL,
        validators=[
            DataRequired(MESSAGE_REQUIRED),
            Email(MESSAGE_EMAIL_INVALID),
            Length(max=EMAIL_MAX_LENGTH),
        ],
    )
    password = PasswordField(
        LABEL_PASSWORD, validators=[DataRequired(MESSAGE_REQUIRED)]
    )
    submit = SubmitField(LABEL_LOGIN_SUBMIT)
