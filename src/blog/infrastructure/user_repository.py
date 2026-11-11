"""
@file
@package blog.infrastructure.user_repository
@brief SQLAlchemy implementation of the user repository port.
"""

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from blog.domain.errors import EmailAlreadyRegisteredError
from blog.domain.user import User
from blog.infrastructure.database import UserModel, db


def _to_domain(row: UserModel) -> User:
    """
    @brief Map a table row to the domain entity.
    @param row The row.
    @return The entity.
    """
    return User(id=row.id, email=row.email, password_hash=row.password, name=row.name)


class SqlAlchemyUserRepository:
    """@brief Stores users through the Flask-SQLAlchemy session."""

    def add(self, user: User) -> User:
        """
        @brief Store a new user.
        @param user The user to store; its id is ignored.
        @return The stored user, with its new id.
        @throws EmailAlreadyRegisteredError When the email is taken.
        """
        row = UserModel(email=user.email, password=user.password_hash, name=user.name)
        db.session.add(row)
        try:
            db.session.commit()
        except IntegrityError as error:
            db.session.rollback()
            raise EmailAlreadyRegisteredError(user.email) from error
        return _to_domain(row)

    def get_by_id(self, user_id: int) -> User | None:
        """
        @brief Read a user by id.
        @param user_id The id.
        @return The user, or None when there is none.
        """
        row = db.session.get(UserModel, user_id)
        return None if row is None else _to_domain(row)

    def get_by_email(self, email: str) -> User | None:
        """
        @brief Read a user by email.
        @param email The email.
        @return The user, or None when there is none.
        """
        row = db.session.scalars(
            select(UserModel).where(UserModel.email == email)
        ).first()
        return None if row is None else _to_domain(row)
