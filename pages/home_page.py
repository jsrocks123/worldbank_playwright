from playwright.sync_api import Page

from pages.base_page import BasePage


class HomePage(BasePage):
    """home page"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.title_text = " Scorecard"
        self.vision_tab = page.locator("//a[contains(@href, 'vision')]")
