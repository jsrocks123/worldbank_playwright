from playwright.sync_api import Page

from components.base_chart import BaseChart


class EndExtremePoverty(BaseChart):
    """end extreme poverty chart"""
    def __init__(self, page: Page):
        self.body = page.locator(
            '//h3[text()="Percentage of population living in poverty (at $2.15/day and $6.85/day) "]'
        )
        super().__init__(page,self.body)
        self.line_tracker_215 = self.line_tracker # orange line
        self.line_tracker_685 = self.page.locator( # blue line
            "//*[local-name()='g' and contains(@class,'highcharts-series-1')]"
            "//*[name()='path' and @class='highcharts-tracker-line']"
        )
        self.more_data = self.page.locator("//a[contains(@href,'SI_POV_DDAY_TO')]")
