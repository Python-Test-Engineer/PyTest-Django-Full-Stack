"""Unit tests for StudyBuddy homepage"""

from http import HTTPStatus

import pytest
from pytest_django.asserts import assertContains, assertTemplateUsed

from django.test import RequestFactory
from django.test import TestCase
from django.urls import reverse

from base.views import home, registerPage

from rich.console import Console

console = Console()

HOMEPAGE_URL = "http://127.0.0.1:8000/"

# add mark for all tests
pytestmark = pytest.mark.django_db


def test_VWS_177_registerPage_returns_correct_response_request_factory():
    """Test registerPage view returns correct response"""
    # Create a request factory
    factory = RequestFactory()

    # Create a GET request
    request = factory.get(HOMEPAGE_URL)

    # Create an instance of the view if CBV
    # view = home.as_view()

    # Call the view with the request
    response = registerPage(request)
    print(response.content[:100])

    # Assert that the response is as expected
    assert response.status_code == 200
    assert b"Register" in response.content
    assertContains(response, "Register")
    # assertTemplateUsed() is only usable on responses fetched using the Django test Client.


def test_VWS_330_registerPage_returns_correct_template_testcase(client):
    url = reverse("register")
    response = client.get(url)
    console.print("\n[cyan]RESPONSE[/]\n")

    form_csrf = str(response.context[1]["csrf_token"])
    form_data = str(response.context[1]["form"])
    # console.print(form_data)

    assertTemplateUsed(response, "base/login_register.html")
    assert response.status_code == HTTPStatus.OK
    assert "password2" in form_data
