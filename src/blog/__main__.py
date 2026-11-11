"""
@file
@package blog.__main__
@brief Entry point: ``python -m blog`` starts the development server.
"""

from blog.constants import DEFAULT_HOST, DEFAULT_PORT
from blog.presentation.app import create_app


def main() -> None:
    """
    @brief Build the application and serve it on the default host and port.
    @return Nothing.
    """
    create_app().run(host=DEFAULT_HOST, port=DEFAULT_PORT)


if __name__ == "__main__":
    main()
