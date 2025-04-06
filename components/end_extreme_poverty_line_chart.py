from playwright.sync_api import Page

from components.base_chart import BaseChart


class EndExtremePoverty(BaseChart):
    def __init__(self, page: Page):
        super().__init__(page)

        self.body = page.locator(
            '//h3[text()="Percentage of population living in poverty (at $2.15/day and $6.85/day) "]'
        )
        self.line_chart_button = (
            self.body.locator("..").locator("..").locator('//button[@id="Line Chart"]')
        )
        self.line_chart_full_screen = (
            self.body.locator("..").locator("..").locator(self.full_screen)
        )
        self.line_chart_close = (
            self.body.locator("..").locator("..").locator(self.close_chart)
        )
        self.line_tracker_215 = (
            self.body.locator("..").locator("..").locator(self.line_tracker)
        )
        self.line_tracker_685 = page.locator(
            "//*[local-name()='g' and contains(@class,'highcharts-series-1')]//*[name()='path' and @class='highcharts-tracker-line']"
        )
        self.more_data = page.locator("//a[contains(@href,'SI_POV_DDAY_TO')]")
