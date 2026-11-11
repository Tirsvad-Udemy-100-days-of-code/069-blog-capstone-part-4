"""
@file
@package blog.infrastructure.clock
@brief The clock port backed by the system time.
"""

from datetime import date, datetime


class SystemClock:
    """@brief Tells today's date from the operating system."""

    def today(self) -> date:
        """
        @brief Read today's date in local time.
        @return Today.
        """
        return datetime.now().astimezone().date()
