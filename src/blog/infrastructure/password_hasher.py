"""
@file
@package blog.infrastructure.password_hasher
@brief The password hasher port backed by Werkzeug.
"""

from werkzeug.security import check_password_hash, generate_password_hash

from blog.constants import PASSWORD_HASH_METHOD, PASSWORD_SALT_LENGTH


class WerkzeugPasswordHasher:
    """@brief Salted PBKDF2 hashes made with Werkzeug."""

    def hash(self, password: str) -> str:
        """
        @brief Make a salted hash of a password.
        @param password The plain password.
        @return The hash, which holds method, salt and digest.
        """
        return generate_password_hash(
            password, method=PASSWORD_HASH_METHOD, salt_length=PASSWORD_SALT_LENGTH
        )

    def verify(self, password_hash: str, password: str) -> bool:
        """
        @brief Check a password against a stored hash.
        @param password_hash The stored hash.
        @param password The plain password to check.
        @return True when they match.
        """
        return check_password_hash(password_hash, password)
