from playwright.sync_api import Page, Locator


class BaseChart:
    """base chart component"""

    def __init__(self, page: Page, body: Locator):
        self.page = page
        self.body = body
        self.line_chart_button = (
            self.body.locator("..").locator("..").locator('//button[@id="Line Chart"]')
        )
        self.full_screen = (
            self.body.locator("..")
            .locator("..")
            .locator('//button[@tooltip="Full Screen"]')
        )
        self.close_chart = (
            self.body.locator("..").locator("..").locator('//span[@tooltip="Close"]')
        )
        self.line_tracker = (
            self.body.locator("..")
            .locator("..")
            .locator(
                '//*[local-name()="g" and contains(@class,"highcharts-series-0")]//*[name()="path" and @class="highcharts-tracker-line"]'
            )
        )
        self.line_chart_tooltip = (
            self.body.locator("..")
            .locator("..")
            .locator(
                '//div[@class="highcharts-label highcharts-tooltip highcharts-color-undefined"]'
            )
        )
