import pytest
from playwright.sync_api import Playwright

from config import SCORECARD_PAGE


@pytest.fixture()
def setup_chrome(playwright: Playwright):
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(SCORECARD_PAGE)
    yield page
    context.close()
