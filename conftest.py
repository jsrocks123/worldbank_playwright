import allure
import pytest
from _pytest.fixtures import FixtureRequest
from playwright.sync_api import Page, Playwright

from config import SCORECARD_PAGE


@pytest.fixture()
def setup_chrome(playwright: Playwright):
    chrome = playwright.chromium
    browser = chrome.launch(headless=True)
    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()
    page.goto(SCORECARD_PAGE)
    yield page
    context.close()


@pytest.fixture(autouse=True)
def attach_playwright_results(page: Page, request: FixtureRequest):
    """Fixture to perform teardown actions and attach results to Allure report
    on failure.

    Args:
        page (Page): Playwright page object.
        request: Pytest request object.
    """
    yield
    if request.node.rep_call.failed:
        allure.attach(
            body=page.url,
            name="URL",
            attachment_type=allure.attachment_type.URI_LIST,
        )
        allure.attach(
            page.screenshot(full_page=True),
            name="Screen shot on failure",
            attachment_type=allure.attachment_type.PNG,
        )
