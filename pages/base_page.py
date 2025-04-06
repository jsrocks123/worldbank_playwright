from playwright.sync_api import Page


class BasePage:
    """base page"""

    def __init__(self, page: Page):
        self.page = page
