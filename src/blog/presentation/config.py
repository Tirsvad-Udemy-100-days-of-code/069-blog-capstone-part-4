"""
@file
@package blog.presentation.config
@brief Application settings: the defaults and the testing configuration.
"""

import os
import secrets
from collections.abc import Mapping
from typing import Final

from blog.constants import (
    DATABASE_FILE_NAME,
    SECRET_KEY_ENV_VAR,
    TESTING_DATABASE_URI,
    TESTING_SECRET_KEY,
)

TESTING_CONFIG: Final[Mapping[str, object]] = {
    "TESTING": True,
    "SECRET_KEY": TESTING_SECRET_KEY,
    "SQLALCHEMY_DATABASE_URI": TESTING_DATABASE_URI,
    "WTF_CSRF_ENABLED": False,
}
"""@brief In-memory database and no CSRF check, for the tests."""


def default_config() -> dict[str, object]:
    """
    @brief Build the settings of a normal run.
    @return The settings; the secret key comes from the environment, or is a
            random value made at startup (sessions then end on restart).
    """
    secret_key = os.environ.get(SECRET_KEY_ENV_VAR) or secrets.token_hex()
    return {
        "SECRET_KEY": secret_key,
        # A relative SQLite path is placed in the instance folder.
        "SQLALCHEMY_DATABASE_URI": f"sqlite:///{DATABASE_FILE_NAME}",
    }
