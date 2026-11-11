"""
@file
@package tests.unit.test_user_use_cases
@brief Tests of the account use cases and the Werkzeug hasher.
"""

import pytest

from blog.application.dto import Registration
from blog.application.user_use_cases import AuthenticateUser, GetUser, RegisterUser
from blog.domain.errors import (
    EmailAlreadyRegisteredError,
    InvalidCredentialsError,
    UnknownEmailError,
)
from blog.infrastructure.password_hasher import WerkzeugPasswordHasher
from tests.unit.fakes import InMemoryUserRepository, ReversingPasswordHasher

REGISTRATION = Registration(email="ann@example.com", password="secret", name="Ann")


def test_register_user_stores_hash_not_plain_password() -> None:
    """@brief The stored user holds the hash and never the plain password."""
    repository = InMemoryUserRepository()
    user = RegisterUser(repository, ReversingPasswordHasher()).execute(REGISTRATION)
    assert user.id == 1
    assert user.password_hash != "secret"
    assert user.name == "Ann"
    assert repository.get_by_email("ann@example.com") == user


def test_register_user_rejects_taken_email() -> None:
    """@brief A second sign-up with the same email is refused."""
    repository = InMemoryUserRepository()
    use_case = RegisterUser(repository, ReversingPasswordHasher())
    use_case.execute(REGISTRATION)
    with pytest.raises(EmailAlreadyRegisteredError):
        use_case.execute(REGISTRATION)
    assert len(repository.users) == 1


def test_authenticate_user_returns_user_for_right_password() -> None:
    """@brief The right email and password give the user."""
    repository = InMemoryUserRepository()
    hasher = ReversingPasswordHasher()
    registered = RegisterUser(repository, hasher).execute(REGISTRATION)
    found = AuthenticateUser(repository, hasher).execute("ann@example.com", "secret")
    assert found == registered


def test_authenticate_user_raises_unknown_email() -> None:
    """@brief An unknown email is its own error."""
    use_case = AuthenticateUser(InMemoryUserRepository(), ReversingPasswordHasher())
    with pytest.raises(UnknownEmailError):
        use_case.execute("nobody@example.com", "x")


def test_authenticate_user_raises_invalid_credentials_for_wrong_password() -> None:
    """@brief A wrong password is a different error from an unknown email."""
    repository = InMemoryUserRepository()
    hasher = ReversingPasswordHasher()
    RegisterUser(repository, hasher).execute(REGISTRATION)
    with pytest.raises(InvalidCredentialsError):
        AuthenticateUser(repository, hasher).execute("ann@example.com", "wrong")


def test_get_user_returns_user_or_none() -> None:
    """@brief A known id gives the user, an unknown id gives None."""
    repository = InMemoryUserRepository()
    hasher = ReversingPasswordHasher()
    registered = RegisterUser(repository, hasher).execute(REGISTRATION)
    assert GetUser(repository).execute(1) == registered
    assert GetUser(repository).execute(2) is None


def test_werkzeug_hasher_hash_differs_from_password_and_verifies() -> None:
    """@brief The hash is salted PBKDF2 and verifies only the right password."""
    hasher = WerkzeugPasswordHasher()
    password_hash = hasher.hash("secret")
    assert password_hash != "secret"
    assert password_hash.startswith("pbkdf2:sha256:")
    assert hasher.verify(password_hash, "secret")
    assert not hasher.verify(password_hash, "other")


def test_werkzeug_hasher_salts_each_hash() -> None:
    """@brief The same password gives different hashes."""
    hasher = WerkzeugPasswordHasher()
    assert hasher.hash("secret") != hasher.hash("secret")
