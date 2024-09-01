from catalog.models import Genre

from rich.console import Console

console = Console()


# The admin client is logged in with a superuser
def test_510_MSC_Genre_changelist(admin_client):
    # https://pytest-django.readthedocs.io/en/latest/helpers.html#admin-client-django-test-client-logged-in-as-admin
    # admin_client is a helper that logins in  a superuser
    genres = [Genre(name="Title" + str(a)) for a in range(0, 20)]
    Genre.objects.bulk_create(genres)
    url = "http://127.0.0.1:8000/admin/catalog/genre/"
    response = admin_client.get(url)
    assert response.status_code == 200

    list_genre_names = list(Genre.objects.values_list("name", flat=True))
    console.print(list_genre_names)
    assert len(list_genre_names) == Genre.objects.count()
