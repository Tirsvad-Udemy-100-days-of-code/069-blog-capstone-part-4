"""
@file
@package blog.infrastructure.database
@brief The Flask-SQLAlchemy extension and the post table.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from blog.constants import (
    DATE_MAX_LENGTH,
    EMAIL_MAX_LENGTH,
    IMG_URL_MAX_LENGTH,
    NAME_MAX_LENGTH,
    PASSWORD_HASH_MAX_LENGTH,
    SUBTITLE_MAX_LENGTH,
    TITLE_MAX_LENGTH,
)


class Base(DeclarativeBase):
    """@brief Declarative base of every table."""


db = SQLAlchemy(model_class=Base)
"""@brief The extension; the composition root binds it to the application."""


class UserModel(Base):
    """@brief Row of the ``users`` table."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(
        String(EMAIL_MAX_LENGTH), unique=True, nullable=False
    )
    password: Mapped[str] = mapped_column(
        String(PASSWORD_HASH_MAX_LENGTH), nullable=False
    )
    name: Mapped[str] = mapped_column(String(NAME_MAX_LENGTH), nullable=False)
    posts: Mapped[list["PostModel"]] = relationship(back_populates="author")


class PostModel(Base):
    """@brief Row of the ``blog_post`` table."""

    __tablename__ = "blog_post"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(TITLE_MAX_LENGTH), nullable=False)
    subtitle: Mapped[str] = mapped_column(String(SUBTITLE_MAX_LENGTH), nullable=False)
    date: Mapped[str] = mapped_column(String(DATE_MAX_LENGTH), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    author: Mapped[UserModel] = relationship(back_populates="posts")
    img_url: Mapped[str] = mapped_column(String(IMG_URL_MAX_LENGTH), nullable=False)
