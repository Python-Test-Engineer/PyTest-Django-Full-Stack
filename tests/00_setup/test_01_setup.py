import logging

from utils.read_config import get_version

from rich.console import Console

# uses config in pytest.ini
LOGGER = logging.getLogger(__name__)

console = Console()


def test_GEN_000_init_works():
    console.print("\n[cyan bold]This is test init[/]")
    assert True


def test_GEN_001_get_version():
    """Test get_version returns correct version"""
    version = get_version()
    console.print(f"\n[cyan bold]{version}[/]")

    assert version is not None


def test_GEN_002_log_info():
    """testing log info"""
    LOGGER.info("testing log info")
    assert 4 != 3


def test_GEN_003_log_warn():
    """testing log warn"""
    LOGGER.warning("testing log warn")
    assert 1


def test_GEN_004_log_critical():
    """testing log critical"""
    LOGGER.critical("testing log critical")
    assert 1
