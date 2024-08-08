"""Some assert examples"""

import pytest


from utils.read_config import get_version

VERSION = "1.0.0"


def test_GEN_001_get_version():
    """Test get_version returns correct version"""
    version = get_version()
    assert version == VERSION
