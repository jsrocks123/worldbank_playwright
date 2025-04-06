from playwright.sync_api import Page

from components.base_chart import BaseChart
from components.end_extreme_poverty_line_chart import EndExtremePoverty
from pages.base_page import BasePage


class VisionPage(BasePage, BaseChart):
    def __init__(self, page: Page):
        BasePage.__init__(self, page)
        BaseChart.__init__(self, page)
        self.title_text = "Measuring Impact | Our Eight High-level Vision Indicators"
        self.end_extreme_poverty = EndExtremePoverty(page)

        self.average_income_shortfall_body = page.locator(
            '//h3[text()="Average income shortfall from a prosperity standard of $25/day "]'
        )
        self.average_income_shortfall_line_chart_button = (
            self.average_income_shortfall_body.locator("..")
            .locator("..")
            .locator('//button[@id="Line Chart"]')
        )
        self.average_income_shortfall_line_chart_full_screen = (
            self.average_income_shortfall_body.locator("..")
            .locator("..")
            .locator(self.full_screen)
        )
        self.average_income_shortfall_line_chart_close = (
            self.average_income_shortfall_body.locator("..")
            .locator("..")
            .locator(self.close_chart)
        )
        self.average_income_shortfall_line_tracker = (
            self.average_income_shortfall_body.locator("..")
            .locator("..")
            .locator(self.line_tracker)
        )
        self.average_income_shortfall_more_data = page.locator(
            "//a[contains(@href,'SI_POV_PROS')]"
        )

        self.economies_with_high_inequality_body = page.locator(
            '//h3[text()="Economies with high inequality "]'
        )
        self.economies_with_high_inequality_line_chart_button = (
            self.economies_with_high_inequality_body.locator("..")
            .locator("..")
            .locator('//button[@id="Line Chart"]')
        )
        self.economies_with_high_inequality_line_chart_full_screen = (
            self.economies_with_high_inequality_body.locator("..")
            .locator("..")
            .locator(self.full_screen)
        )
        self.economies_with_high_inequality_line_chart_close = (
            self.economies_with_high_inequality_body.locator("..")
            .locator("..")
            .locator(self.close_chart)
        )
        self.economies_with_high_inequality_line_tracker = (
            self.economies_with_high_inequality_body.locator("..")
            .locator("..")
            .locator(self.line_tracker)
        )
        self.economies_with_high_inequality_more_data = page.locator(
            "//a[contains(@href,'SI_DST_INEQ')]"
        )
