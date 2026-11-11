"""
@file
@package blog.infrastructure.database
@brief The Flask-SQLAlchemy extension and the post table.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from blog.constants import (
    AUTHOR_MAX_LENGTH,
    DATE_MAX_LENGTH,
    IMG_URL_MAX_LENGTH,
    SUBTITLE_MAX_LENGTH,
    TITLE_MAX_LENGTH,
)


class Base(DeclarativeBase):
    """@brief Declarative base of every table."""


db = SQLAlchemy(model_class=Base)
"""@brief The extension; the composition root binds it to the application."""


class PostModel(Base):
    """@brief Row of the ``blog_post`` table."""

    __tablename__ = "blog_post"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(TITLE_MAX_LENGTH), nullable=False)
    subtitle: Mapped[str] = mapped_column(String(SUBTITLE_MAX_LENGTH), nullable=False)
    date: Mapped[str] = mapped_column(String(DATE_MAX_LENGTH), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(AUTHOR_MAX_LENGTH), nullable=False)
    img_url: Mapped[str] = mapped_column(String(IMG_URL_MAX_LENGTH), nullable=False)
