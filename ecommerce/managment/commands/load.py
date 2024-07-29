import random

from django.core.management.base import BaseCommand
from base.models import User
from django.utils import timezone
from rich.console import Console

console = Console()


class Command(BaseCommand):
    help = "Creates application data"

    def handle(self, *args, **kwargs):
        # get or create an admin user
        console.print("[green]Creating admin user...[/green]")
        user = User.objects.filter(username="admin")
        if not user.exists():
            user = User.objects.create_superuser(username="admin", password="test")
        else:
            user = user.first()
