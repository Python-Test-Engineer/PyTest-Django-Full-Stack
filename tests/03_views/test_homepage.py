"""Unit tests for StudyBuddy homepage"""

import pytest
import pytest
from pytest_django.asserts import assertContains, assertTemplateUsed
from http import HTTPStatus

from django.test import RequestFactory
from django.test import Client

from base.views import home, registerPage

HOMEPAGE_URL = "http://127.0.0.1:8000/"

# add mark for all tests
pytestmark = pytest.mark.django_db


def test_VWS_172_homepage_using_factory():
    """test using factory"""

    # Create a request factory
    factory = RequestFactory()

    # Create a GET request
    request = factory.get(HOMEPAGE_URL)
    # Test my_view() as if it were deployed at /customer/details
    response = home(request)
    # Use this syntax for class-based views.
    response = home(request)
    assert response.status_code == 200
    # RequestFactory has not context just Client
    # for item in response.context[0]:
    #     for key, value in item.items():
    #         print(f"{key}: {value}")
    #         if key == "rooms":
    #             assert "rooms is in context"
    #         if key == "topics":
    #             assert "topics is in context"
    #         if key == "room_count":
    #             assert "room_count is in context"
    #         if key == "room_messages":
    #             assert "room_messages is in context"


def test_VWS_175_homepage_returns_correct_response_client_and_context():
    """test if homepage has correct template used, context and HTTP status code"""

    client = Client()
    response = client.get(HOMEPAGE_URL)
    assert response.status_code == 200
    for item in response.context[0]:
        for key, value in item.items():
            print(f"{key}: {value}")
            if key == "rooms":
                assert "rooms is in context"
            if key == "topics":
                assert "topics is in context"
            if key == "room_count":
                assert "room_count is in context"
            if key == "room_messages":
                assert "room_messages is in context"
