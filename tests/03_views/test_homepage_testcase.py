"""Unit tests for StudyBuddy homepage"""

from http import HTTPStatus


from base.views import registerPage, home
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase


HOMEPAGE_URL = "http://127.0.0.1:8000/"


class TestHomePage(TestCase):
    """test home page"""

    def setUp(self) -> None:
        self.factory = RequestFactory()
        print(f"\nHomepage: {HOMEPAGE_URL}")

    def test_VWS_170_homepage_returns_correct_response(self):
        """test if homepage has correct template used and HTTP status code"""
        response = self.client.get(HOMEPAGE_URL)
        print(f"\nResponse code: {response.status_code}")
        self.assertTemplateUsed(response, "base/home.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_VWS_171_homepage_returns_correct_title(self):
        """Test if homepage has correct title"""
        response = self.client.get(HOMEPAGE_URL)
        print(f"\nResponse: {response}")
        self.assertContains(response, "<h2>Study Rooms</h2>")

    def test_VWS_172_homepage_using_factory(self):
        """test using factory"""

        request = self.factory.get(HOMEPAGE_URL)

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        # request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = home(request)
        # Use this syntax for class-based views.
        response = home(request)
        self.assertEqual(response.status_code, 200)
