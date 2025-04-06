from playwright.sync_api import Page

from components.base_table import BaseTable
from pages.base_page import BasePage


class IndicatorDetail_SI_DST_INEQ(BasePage, BaseTable):
    def __init__(self, page: Page):
        BasePage.__init__(self, page)
        BaseTable.__init__(self, page)
        self.title_text = (
            "Economies with high inequality | Scorecard - World Bank Group"
        )
