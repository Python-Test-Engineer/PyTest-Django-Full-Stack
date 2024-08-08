"""Some assert examples"""

from time import sleep
import logging

import pytest

# uses config in pytest.ini
LOGGER = logging.getLogger(__name__)


def test_GEN_002_log_info():
    """testing log info"""
    LOGGER.info("testing log info")
    assert 4 != 3


def test_GEN_003_log_warn():
    """testing log warn"""
    LOGGER.warn("testing log warn")
    assert 1


def test_GEN_004_log_critical():
    """testing log critical"""
    LOGGER.critical("testing log critical")
    assert 1
