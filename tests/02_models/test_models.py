from django.test import TestCase
from catalog.models import Genre, Author
from rich.console import Console

console = Console()


class TestGenre(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.genre_obj = Genre.objects.create(name="TestGenre")
        console.print(cls.genre_obj.__dict__)
        # Create authors for pagination tests
        cls.author_obj = Author.objects.create(first_name="First", last_name="Last")
        console.print(cls.author_obj.__dict__)
        # Create authors for pagination tests

    def test_MDL_201_genre_str(self):

        self.assertEqual(str(self.genre_obj), f"Genre: {self.genre_obj.name}")

    def test_MDL_202_genre_str_dunder(self):

        self.assertEqual(self.genre_obj.__str__(), f"Genre: {self.genre_obj.name}")

    def test_MDL_203_genre_absolute_url(self):

        self.assertEqual(self.genre_obj.get_absolute_url(), "/catalog/genre/1")

    def test_MDL_203_author_absolute_url(self):

        self.assertEqual(self.genre_obj.get_absolute_url(), "/catalog/genre/1")

    def test_MDL_204_author_str(self):

        self.assertEqual(
            self.author_obj.__str__(),
            f"{self.author_obj.last_name}, {self.author_obj.first_name}",
        )
