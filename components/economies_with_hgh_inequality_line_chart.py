from playwright.sync_api import Page

from components.base_chart import BaseChart


class EconomiesWithHighInequality(BaseChart):
    """economies with high inequality chart"""
    def __init__(self, page: Page):
        self.body = page.locator('//h3[text()="Economies with high inequality "]')
        super().__init__(page,self.body)
        self.more_data = self.page.locator("//a[contains(@href,'SI_DST_INEQ')]")
