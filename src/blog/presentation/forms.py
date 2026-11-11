"""
@file
@package blog.presentation.forms
@brief The post form.
"""

from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

from blog.application.dto import PostContent
from blog.constants import (
    AUTHOR_MAX_LENGTH,
    IMG_URL_MAX_LENGTH,
    IMG_URL_PATTERN,
    LABEL_AUTHOR,
    LABEL_BODY,
    LABEL_IMG_URL,
    LABEL_SUBMIT,
    LABEL_SUBTITLE,
    LABEL_TITLE,
    MESSAGE_IMG_URL_INVALID,
    MESSAGE_REQUIRED,
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
    author = StringField(
        LABEL_AUTHOR,
        validators=[DataRequired(MESSAGE_REQUIRED), Length(max=AUTHOR_MAX_LENGTH)],
    )
    body = CKEditorField(LABEL_BODY, validators=[DataRequired(MESSAGE_REQUIRED)])
    submit = SubmitField(LABEL_SUBMIT)

    def to_content(self) -> PostContent:
        """
        @brief Read the validated fields as use case input.
        @return What the author wrote.
        """
        return PostContent(
            title=self.title.data or "",
            subtitle=self.subtitle.data or "",
            img_url=self.img_url.data or "",
            author=self.author.data or "",
            body=self.body.data or "",
        )
