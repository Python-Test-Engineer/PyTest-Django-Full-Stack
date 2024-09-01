"""Based on https://www.youtube.com/watch?v=_8qLxaWMdzE DjangoCon 2021 | Speed up your tests with setUpTestData | Adam Johnson

This shows that with setUpTestData the changes are rolled back after each test.

"""

from catalog.models import Genre
from django.test import TestCase
from rich.console import Console

console = Console()


class TestSetUp01(TestCase):

    def setUp(self):
        # super().setUp() # these supers are only needed if we have redefined the setUp method.
        console.print("\n[green bold]SETUP[/]")
        self.user = "START"

    def tearDown(self):

        if hasattr(self, "user"):
            self.user = "END"
            # super().tearDown()
            console.print("[red bold]TEARDOWN[/]")

    def test_GEN_10_first(self):
        console.print("[cyan bold]Running test_GEN_10_first...[/]")
        assert True

    def test_GEN_10_second(self):
        console.print("[cyan bold]Running test_GEN_10_second...[/]")
        assert True

    def test_GEN_10_third(self):
        console.print("[cyan bold]Running test_GEN_10_third...[/]")
        assert True
