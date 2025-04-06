from playwright.sync_api import Page

from components.base_table import BaseTable
from pages.base_page import BasePage


class IndicatorDetail_SI_POV_DDAY_TO(BasePage, BaseTable):
    def __init__(self, page: Page):
        BasePage.__init__(self, page)
        BaseTable.__init__(self, page)
        self.title_text = "Percentage of population living in poverty (at $2.15/day and $6.85/day) | Scorecard - World Bank Group"

    def get_table_data(self):
        table_data = {}
        for i in range(self.row_count):
            left_column_cell = self.left_column.locator(
                self._selectors.ROW_ID.replace("##row_id##", f"{i}")
            )
            left_column_cell.scroll_into_view_if_needed()
            left_column_cell_value = left_column_cell.locator(
                self._selectors.LEFT_COLUMN_CELL_TEXT
            ).text_content()
            value_row = self.right_columns.locator(
                self._selectors.ROW_ID.replace("##row_id##", f"{i}")
            )
            value_215 = value_row.locator(
                self._selectors.VALUE_COLUMN.replace(
                    "##value##", "SI_POV_DDAY_achievedBaseVal"
                )
            ).text_content()
            year = value_row.locator(
                f"{self._selectors.YEAR_COLUMN.replace(
                        "##year##", "SI_POV_DDAY_latestYear"
                    )}/span"
            ).text_content()
            value_685 = value_row.locator(
                self._selectors.VALUE_COLUMN.replace(
                    "##value##", "SI_POV_UMIC_achievedBaseVal"
                )
            ).text_content()
            table_data[left_column_cell_value] = {year: [value_215, value_685]}
        return table_data
