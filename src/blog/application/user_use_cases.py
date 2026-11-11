"""
@file
@package blog.application.user_use_cases
@brief The things a visitor can do about an account.
"""

from blog.application.dto import Registration
from blog.application.ports import PasswordHasher
from blog.domain.errors import (
    EmailAlreadyRegisteredError,
    InvalidCredentialsError,
    UnknownEmailError,
)
from blog.domain.user import User, normalise_email
from blog.domain.user_repository import UserRepository


class RegisterUser:
    """@brief Create an account with a hashed password."""

    def __init__(self, repository: UserRepository, hasher: PasswordHasher) -> None:
        """
        @brief Create the use case.
        @param repository Where users are stored.
        @param hasher Makes the password hash.
        """
        self._repository = repository
        self._hasher = hasher

    def execute(self, registration: Registration) -> User:
        """
        @brief Run the use case.
        @param registration What the person entered.
        @return The stored user; only the hash of the password is kept.
        @throws EmailAlreadyRegisteredError When the email is taken.
        """
        email = normalise_email(registration.email)
        if self._repository.get_by_email(email) is not None:
            raise EmailAlreadyRegisteredError(email)
        user = User(
            id=None,
            email=email,
            password_hash=self._hasher.hash(registration.password),
            name=registration.name,
        )
        return self._repository.add(user)


class AuthenticateUser:
    """@brief Check an email and password."""

    def __init__(self, repository: UserRepository, hasher: PasswordHasher) -> None:
        """
        @brief Create the use case.
        @param repository Where users are stored.
        @param hasher Checks the password.
        """
        self._repository = repository
        self._hasher = hasher

    def execute(self, email: str, password: str) -> User:
        """
        @brief Run the use case.
        @param email The email entered.
        @param password The password entered.
        @return The user the credentials belong to.
        @throws UnknownEmailError When no user has the email.
        @throws InvalidCredentialsError When the password does not match.
        """
        user = self._repository.get_by_email(normalise_email(email))
        if user is None:
            raise UnknownEmailError(email)
        if not self._hasher.verify(user.password_hash, password):
            raise InvalidCredentialsError
        return user


class GetUser:
    """@brief Read one user by id."""

    def __init__(self, repository: UserRepository) -> None:
        """
        @brief Create the use case.
        @param repository Where users are stored.
        """
        self._repository = repository

    def execute(self, user_id: int) -> User | None:
        """
        @brief Run the use case.
        @param user_id The id.
        @return The user, or None when there is none.
        """
        return self._repository.get_by_id(user_id)
