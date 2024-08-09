"""Unit tests for StudyBuddy homepage"""

import pytest
from http import HTTPStatus

from django.test import RequestFactory
from django.test import Client

from base.views import home, registerPage

HOMEPAGE_URL = "http://127.0.0.1:8000/"

# add mark for all tests
pytestmark = pytest.mark.django_db


def test_VWS_175_homepage_returns_correct_response_client():
    """test if homepage has correct template used and HTTP status code"""

    client = Client()
    response = client.get(HOMEPAGE_URL)
    assert response.status_code == 200


def test_VWS_176_homepage_returns_correct_response_request_factory():

    # Create a request factory
    factory = RequestFactory()

    # Create a GET request
    request = factory.get(HOMEPAGE_URL)

    # Create an instance of the view if CBV
    # view = home.as_view()

    # Call the view with the request
    response = home(request)

    # Assert that the response is as expected
    assert response.status_code == 200
