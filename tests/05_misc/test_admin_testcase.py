from django.test import TestCase, Client
from django.contrib.auth.models import User

from rich.console import Console

console = Console()


class TestAdminPanel(TestCase):
    def create_user(self):
        self.username = "test_admin"
        self.password = "fdfdfdas"
        user, created = User.objects.get_or_create(username=self.username)
        user.set_password(self.password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        self.user = user
        console.print(f"Created user:\n {self.user.__dict__}")

    def test_511_MSC_spider_admin(self):
        self.create_user()
        client = Client()
        client.login(username=self.username, password=self.password)
        admin_pages = [
            "/admin/",
            # put all the admin pages for your models in here.
            "/admin/auth/",
            "/admin/auth/group/",
            "/admin/auth/group/add/",
            "/admin/auth/user/",
            "/admin/auth/user/add/",
            "/admin/password_change/",
            "/admin/catalog/genre/",
            "/admin/catalog/genre/add/",
            "/admin/catalog/author/add/",
        ]
        for page in admin_pages:
            console.print(f"[green]Testing {page}[/]")
            resp = client.get(page)
            assert resp.status_code == 200
            assert b"<!DOCTYPE html" in resp.content
