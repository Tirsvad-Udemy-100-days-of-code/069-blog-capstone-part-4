"""
@file
@package tests.unit.conftest
@brief Fixtures for the unit tests.
"""

from datetime import date

import pytest

from tests.unit.fakes import FixedClock, InMemoryPostRepository


@pytest.fixture
def repository() -> InMemoryPostRepository:
    """
    @brief Provide an empty fake repository.
    @return The repository.
    """
    return InMemoryPostRepository()


@pytest.fixture
def clock() -> FixedClock:
    """
    @brief Provide a clock fixed on 5 November 2026.
    @return The clock.
    """
    return FixedClock(date(2026, 11, 5))
