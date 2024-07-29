"""Some assert examples"""

from time import sleep
import logging

import pytest

# uses config in pytest.ini
LOGGER = logging.getLogger(__name__)


def test_0008_a1():
    """A test"""
    LOGGER.info("test_a1")
    assert 4 != 3


def test_0009_a2():
    """A test"""
    LOGGER.warn("test_a2")
    assert 1


def test_0001_a3():
    """A test"""
    LOGGER.critical("critical test 0001")
    assert 1
