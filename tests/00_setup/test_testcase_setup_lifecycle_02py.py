"""Based on https://www.youtube.com/watch?v=_8qLxaWMdzE DjangoCon 2021 | Speed up your tests with setUpTestData | Adam Johnson

https://github.com/adamchainz/talk-speed-up-your-tests-with-setuptestdata
"""

from catalog.models import Genre
from django.test import TestCase
from rich.console import Console

console = Console()


class TestSetUp02(TestCase):

    @classmethod
    def setUpTestData(cls):
        console.print("\n[green bold]setUpTestData...[/]")
        cls.genre = Genre.objects.create(name="Isolation")
        is_in_db = Genre.objects.get(name="Isolation")
        console.print(
            f"[cyan bold]Just created '{is_in_db}' is in DB[/]\nThis will be IN MEMORY too."
        )

    def setUp(self):
        # This would be called before each test e.g self.client.force_login(self.user)
        pass

    def test_GEN_011_that_changes_genre(self):
        console.print("[cyan bold]Running test_GEN_011_that_changes_genre...[/]")
        self.genre.name == "NO Isolation"
        is_in_db = Genre.objects.get(name="Isolation")
        console.print(
            f"[green italic]Is '{is_in_db}' in DB? {is_in_db in Genre.objects.all()}[/]"
        )
        # self.genre.name will rollback after test so later tests will see the original name

    def test_GEN_011_that_reads_genre_from_db(self):
        console.print("[cyan bold]Running test_GEN_011_that_reads_genre_from_db...[/]")
        is_in_db = Genre.objects.get(name="Isolation")
        console.print(
            f"[green italic]Is '{is_in_db}' in DB? {is_in_db in Genre.objects.all()}[/]"
        )
        assert is_in_db.name == "Isolation"

    def test_GEN_011_that_reads_in_memory_genre(self):
        console.print(
            "[cyan bold]Running test_GEN_011_that_reads_in_memory_genre...[/]"
        )
        console.print("This passes because the in memory change is rolled back.")
        is_in_db = Genre.objects.get(name="Isolation")
        console.print(
            f"[green italic]Is '{is_in_db}' in DB? {is_in_db in Genre.objects.all()}[/]"
        )
        console.print(
            f"[green italic]Has in memorychanged? [/][red]{self.genre.name == 'NO Isolation'}.[/][green italic] In mememory is '{self.genre.name}'[/]"
        )
        assert self.genre.name != "NO Isolation"
