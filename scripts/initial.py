import random

from django.core.management.base import BaseCommand
from base.models import User
from django.utils import timezone
from rich.console import Console


console = Console()


def run():
    # enter code below
    console.print("[green]Testing django-extensions script...[/green]")
