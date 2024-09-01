"""Testing Pets API"""

import pytest

from utils.api_utils import delete_data, get_api_data, put_data
from utils.read_config import get_locallibrary_api_url

from rich.console import Console

console = Console()

basebase_url = get_locallibrary_api_url()

# Ensure site is running


def test_url() -> None:
    """Testing URL"""
    print(basebase_url)
    assert basebase_url


def test_0170_API_get_employees() -> None:
    """Testing GET"""
    url = basebase_url
    data, resp_status, time_taken = get_api_data(url)
    console.print(data[0])
    assert resp_status == 200
    assert data[0]["first_name"] == "James"
    assert data[0]["last_name"] == "Harry"
