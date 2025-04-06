from playwright.sync_api import Page


class BaseChart:
    def __init__(self, page: Page):
        self.page = page
        self.full_screen = page.locator("//button[@tooltip='Full Screen']")
        self.close_chart = page.locator("//span[@tooltip='Close']")
        self.line_tracker = page.locator(
            "//*[local-name()='g' and contains(@class,'highcharts-series-0')]"
            "//*[name()='path' and @class='highcharts-tracker-line']"
        )
        self.line_chart_tooltip = page.locator(
            "//div[@class='highcharts-label highcharts-tooltip highcharts-color-undefined']"
        )
