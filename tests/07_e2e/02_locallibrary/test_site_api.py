from django.test import LiveServerTestCase
from playwright.sync_api import Page, expect
import re
import pytest

from playwright.sync_api import sync_playwright
from rich.console import Console

console = Console()


@pytest.mark.skip(reason="needs server running")
def test_750_E2E_login_then_get_title(page: Page) -> None:
    """Needs server running"""
    page.goto("http://127.0.0.1:8000/accounts/login/?next=/catalog/")
    page.locator("html").click()
    page.get_by_label("Username:").click()
    page.get_by_label("Username:").fill("admin")
    page.get_by_label("Password:").fill("password@2024")
    page.get_by_role("button", name="login").click()
    expect(page).to_have_title(re.compile("Local Library"))


class MyPlaywrightTests(LiveServerTestCase):
    def test_753_E2Epage(self):

        with sync_playwright() as playwright:
            engine = playwright.chromium
            browser = engine.launch()
            context = browser.new_context()
            page = context.new_page()
            console.print(
                f"[blue bold]Using: {self.live_server_url}/catalog/[/blue bold]"
            )
            console.print(
                f"[dark_orange italic]Note using a random port {self.live_server_url}[/]"
            )
            page.goto(f"{self.live_server_url}/catalog/")
            page.get_by_role("link", name="Login").click()
            page.get_by_label("Username:").click()
            page.get_by_label("Username:").fill("admin")
            page.get_by_label("Username:").press("Tab")
            page.get_by_label("Password:").fill("password@2024")
            page.get_by_role("button", name="login").click()
            page.locator("html")
            expect(page).to_have_title(re.compile("Local Library"))
            browser.close()
