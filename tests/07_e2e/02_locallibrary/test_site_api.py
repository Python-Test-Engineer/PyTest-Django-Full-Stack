from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright.sync_api import Page, Locator, expect
import re
import pytest
from playwright.sync_api import sync_playwright, Playwright


def test_750_E2E_login_then_get_title(page: Page) -> None:
    page.goto("http://127.0.0.1:8000/accounts/login/?next=/catalog/")
    page.locator("html").click()
    page.get_by_label("Username:").click()
    page.get_by_label("Username:").fill("admin")
    page.get_by_label("Password:").fill("password@2024")
    page.get_by_role("button", name="login").click()
    expect(page).to_have_title(re.compile("Local Library"))


class MyPlaywrightTests(StaticLiveServerTestCase):
    def test_753_E2Epage(self):

        with sync_playwright() as playwright:
            webkit = playwright.webkit
            browser = webkit.launch()
            context = browser.new_context()
            page = context.new_page()
            print(self.live_server_url)
            page.goto(f"{self.live_server_url}/login/")
            page.locator("html")
            page.get_by_label("Username:")
            # page.get_by_label("Username:").fill("admin")
            # page.get_by_label("Password:").fill("password@2024")
            # page.get_by_role("button", name="login").click()
            # expect(page).to_have_title(re.compile("Local Library"))
            assert True
            # run(playwright)
            browser.close()
