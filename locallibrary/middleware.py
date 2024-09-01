"""Middleware for locallibrary project.
Based on BugBytes https://www.youtube.com/watch?v=TTEEr4N-lKw&t
"""

from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from rich.console import Console

console = Console()


class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # console.log("[green]Request Received[/]")
        if settings.MAINTENANCE_MODE:
            console.log("[red bold]Application is in maintenance mode![/]")
            # return HttpResponse("Application is in maintenance mode!")
            return render(request, "maintenance_mode_on.html")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
