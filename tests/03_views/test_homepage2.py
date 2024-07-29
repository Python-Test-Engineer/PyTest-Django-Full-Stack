"""Unit tests for StudyBuddy homepage"""

from http import HTTPStatus


from base.views import registerPage, home
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase, Client


HOMEPAGE_URL = "http://127.0.0.1:8000/"


class TestHomePage(TestCase):
    """test home page"""

    def setUp(self):
        self.client = Client()

    def test_hello_world_view(self):
        response = self.client.get(HOMEPAGE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "!DOC")
        self.assertContains(response, "<h2>Study Rooms</h2>")
