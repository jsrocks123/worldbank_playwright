from playwright.sync_api import Page

from components.average_income_shortfall_line_chart import AverageIncomeShortfall
from components.economies_with_hgh_inequality_line_chart import (
    EconomiesWithHighInequality,
)
from components.end_extreme_poverty_line_chart import EndExtremePoverty
from pages.base_page import BasePage


class VisionPage(BasePage):
    """vision page"""

    def __init__(self, page: Page):
        BasePage.__init__(self, page)
        self.title_text = "Measuring Impact | Our Eight High-level Vision Indicators"
        self.end_extreme_poverty = EndExtremePoverty(page)
        self.average_income_shortfall = AverageIncomeShortfall(page)
        self.economies_with_high_inequality = EconomiesWithHighInequality(page)
