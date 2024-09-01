from django.contrib.auth.models import (
    Permission,
)  # Required to grant the permission needed to set a book as returned.
import datetime
from django.utils import timezone
from catalog.models import BookInstance, Book, Genre, Language
from django.contrib.auth import get_user_model
from django.test import TestCase
from catalog.models import Author
from django.urls import reverse
from rich.console import Console

console = Console()
User = get_user_model()

# collectstatic needs to be run so that tests pass


class RenewBookInstancesViewTest(TestCase):

    def setUp(self):
        # Create a user
        test_user1 = User.objects.create_user(
            username="testuser1", password="1X<ISRUkw+tuK"
        )
        test_user1.save()

        test_user2 = User.objects.create_user(
            username="testuser2", password="2HJ1vRV0Z&3iD"
        )
        test_user2.save()
        permission = Permission.objects.get(name="Set book as returned")
        test_user2.user_permissions.add(permission)
        test_user2.save()

        # Create a book
        test_author = Author.objects.create(first_name="John", last_name="Smith")
        test_genre = Genre.objects.create(name="Fantasy")
        test_language = Language.objects.create(name="English")
        test_book = Book.objects.create(
            title="Book Title",
            summary="My book summary",
            isbn="ABCDEFG",
            author=test_author,
            language=test_language,
        )
        # Create genre as a post-step
        genre_objects_for_book = Genre.objects.all()
        test_book.genre.set(genre_objects_for_book)
        test_book.save()

        # Create a BookInstance object for test_user1
        return_date = datetime.date.today() + datetime.timedelta(days=5)
        self.test_bookinstance1 = BookInstance.objects.create(
            book=test_book,
            imprint="Unlikely Imprint, 2016",
            due_back=return_date,
            borrower=test_user1,
            status="o",
        )

        # Create a BookInstance object for test_user2
        return_date = datetime.date.today() + datetime.timedelta(days=5)
        self.test_bookinstance2 = BookInstance.objects.create(
            book=test_book,
            imprint="Unlikely Imprint, 2016",
            due_back=return_date,
            borrower=test_user2,
            status="o",
        )

    def test_411_FRM_view_redirect_if_not_logged_in(self):
        """
        Test that if a user is not logged in and tries to access the FRM 'renew-book-librarian' view,
        they are redirected to the login page.
        """
        response = self.client.get(
            reverse("renew-book-librarian", kwargs={"pk": self.test_bookinstance1.pk})
        )
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith("/accounts/login/"))

    def test_412_FRM_view_forbidden_if_logged_in_but_not_correct_permission(self):
        login = self.client.login(username="testuser1", password="1X<ISRUkw+tuK")
        response = self.client.get(
            reverse("renew-book-librarian", kwargs={"pk": self.test_bookinstance1.pk})
        )
        self.assertEqual(response.status_code, 403)

    def test_413_FRM_view_success_if_logged_in_with_permission_borrowed_book(self):
        login = self.client.login(username="testuser2", password="2HJ1vRV0Z&3iD")
        response = self.client.get(
            reverse("renew-book-librarian", kwargs={"pk": self.test_bookinstance2.pk})
        )

        # Check that it lets us login - this is our book and we have the right permissions.
        self.assertEqual(response.status_code, 200)

    def test_414_FRM_view_forbidden_if_logged_in_with_permission_another_users_borrowed_book(
        self,
    ):
        login = self.client.login(username="testuser2", password="2HJ1vRV0Z&3iD")
        response = self.client.get(
            reverse("renew-book-librarian", kwargs={"pk": self.test_bookinstance1.pk})
        )

        # Check that it lets us login. We're a librarian, so we can view any users book
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        login = self.client.login(username="testuser2", password="2HJ1vRV0Z&3iD")
        response = self.client.get(
            reverse("renew-book-librarian", kwargs={"pk": self.test_bookinstance1.pk})
        )
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, "catalog/book_renew_librarian.html")

    def test_415_form_renewal_date_initially_has_date_three_weeks_in_future(self):
        login = self.client.login(username="testuser2", password="2HJ1vRV0Z&3iD")
        response = self.client.get(
            reverse("renew-book-librarian", kwargs={"pk": self.test_bookinstance1.pk})
        )
        self.assertEqual(response.status_code, 200)

        date_3_weeks_in_future = datetime.date.today() + datetime.timedelta(weeks=3)
        self.assertEqual(
            response.context["form"].initial["renewal_date"], date_3_weeks_in_future
        )

    def test_416_FRM_form_invalid_renewal_date_past(self):
        login = self.client.login(username="testuser2", password="2HJ1vRV0Z&3iD")

        date_in_past = datetime.date.today() - datetime.timedelta(weeks=1)
        response = self.client.post(
            reverse("renew-book-librarian", kwargs={"pk": self.test_bookinstance1.pk}),
            {"renewal_date": date_in_past},
        )
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response.context["form"], "renewal_date", "Invalid date - renewal in past"
        )

    def test_420_FRM_form_invalid_renewal_date_future(self):
        login = self.client.login(username="testuser2", password="2HJ1vRV0Z&3iD")

        invalid_date_in_future = datetime.date.today() + datetime.timedelta(weeks=5)
        response = self.client.post(
            reverse("renew-book-librarian", kwargs={"pk": self.test_bookinstance1.pk}),
            {"renewal_date": invalid_date_in_future},
        )
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response.context["form"],
            "renewal_date",
            "Invalid date - renewal more than 4 weeks ahead",
        )

    def test_417_FRM_redirects_to_all_borrowed_book_list_on_success(self):
        login = self.client.login(username="testuser2", password="2HJ1vRV0Z&3iD")
        valid_date_in_future = datetime.date.today() + datetime.timedelta(weeks=2)
        response = self.client.post(
            reverse("renew-book-librarian", kwargs={"pk": self.test_bookinstance1.pk}),
            {"renewal_date": valid_date_in_future},
        )
        self.assertRedirects(response, reverse("all-borrowed"))

    def test_418_FRM_HTTP404_for_invalid_book_if_logged_in(self):
        import uuid

        test_uid = uuid.uuid4()  # unlikely UID to match our bookinstance!
        login = self.client.login(username="testuser2", password="2HJ1vRV0Z&3iD")
        response = self.client.get(
            reverse("renew-book-librarian", kwargs={"pk": test_uid})
        )
        self.assertEqual(response.status_code, 404)


from django.contrib.contenttypes.models import ContentType


class AuthorCreateViewTest(TestCase):
    """Test case for the AuthorCreate view (Created as Challenge)."""

    def setUp(self):
        # Create a user
        test_user1 = User.objects.create_user(
            username="testuser1", password="1X<ISRUkw+tuK"
        )
        test_user2 = User.objects.create_user(
            username="testuser2", password="2HJ1vRV0Z&3iD"
        )

        test_user1.save()
        test_user2.save()

        content_typeBook = ContentType.objects.get_for_model(Book)

        permAddBook = Permission.objects.get(
            codename="add_book",
            content_type=content_typeBook,
        )

        content_typeAuthor = ContentType.objects.get_for_model(Author)
        permAddAuthor = Permission.objects.get(
            codename="add_author",
            content_type=content_typeAuthor,
        )

        test_user2.user_permissions.add(permAddBook, permAddAuthor)
        test_user2.save()

        # Create a book
        test_author = Author.objects.create(first_name="John", last_name="Smith")

    def test_420_FRM_view_with_redirect_if_not_logged_in(self):
        response = self.client.get(reverse("author-create"))
        self.assertRedirects(response, "/accounts/login/?next=/catalog/author/create/")

    def test_421_FRM_view_with_forbidden_if_logged_in_but_not_correct_permission(self):
        login = self.client.login(username="testuser1", password="1X<ISRUkw+tuK")
        response = self.client.get(reverse("author-create"))
        self.assertEqual(response.status_code, 403)

    def test_422_FRM_view_with_forbidden_if_logged_in_with_permission(self):
        login = self.client.login(username="testuser2", password="2HJ1vRV0Z&3iD")
        response = self.client.get(reverse("author-create"))
        self.assertEqual(response.status_code, 200)

    def test_431_FRM_view_uses_correct_template(self):
        login = self.client.login(username="testuser2", password="2HJ1vRV0Z&3iD")
        response = self.client.get(reverse("author-create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/author_form.html")

    def test_432_FRM_form_date_of_death_initially_set_to_expected_date(self):
        login = self.client.login(username="testuser2", password="2HJ1vRV0Z&3iD")
        response = self.client.get(reverse("author-create"))
        self.assertEqual(response.status_code, 200)

        expected_initial_date = datetime.date(2023, 11, 11)
        response_date = response.context["form"].initial["date_of_death"]
        response_date = datetime.datetime.strptime(response_date, "%d/%m/%Y").date()
        self.assertEqual(response_date, expected_initial_date)

    def test_433_FRM_redirects_to_detail_view_on_success(self):
        login = self.client.login(username="testuser2", password="2HJ1vRV0Z&3iD")
        response = self.client.post(
            reverse("author-create"),
            {"first_name": "Christian Name", "last_name": "Surname"},
        )
        # Manually check redirect because we don't know what author was created
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith("/catalog/author/"))
