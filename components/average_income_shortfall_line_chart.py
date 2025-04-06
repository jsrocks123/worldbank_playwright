from playwright.sync_api import Page

from components.base_chart import BaseChart


class AverageIncomeShortfall(BaseChart):
    """average income shortfall chart"""

    def __init__(self, page: Page):
        self.body = page.locator(
            '//h3[text()="Average income shortfall from a prosperity standard of $25/day "]'
        )
        super().__init__(page, self.body)
        self.more_data = self.page.locator("//a[contains(@href,'SI_POV_PROS')]")
