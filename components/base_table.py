from playwright.sync_api import Page


class BaseTable:
    """base table component"""

    def __init__(self, page: Page):
        self.page = page
        self._selectors = self._Selectors()
        self.table = page.locator("//div[@role='treegrid']")
        self.row_count = int(self.table.get_attribute("aria-rowcount")) - 2
        self.left_column = self.page.locator("//div[@class='ag-center-cols-container']")
        self.left_column_cell_text = self.page.locator("//div[@class='text-ellipsis']")
        self.right_columns = self.page.locator(
            "//div[@class='ag-pinned-right-cols-container']"
        )

    class _Selectors:
        """selector strings"""

        ROW_ID = "//div[@row-id='##row_id##']"
        LEFT_COLUMN_CELL_TEXT = "//div[@class='text-ellipsis']"
        VALUE_COLUMN = "//div[@col-id='##value##']/span"
        YEAR_COLUMN = "//div[@col-id='##year##']"

    def get_table_data(self):
        """retrieve data from all rows and columns"""
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
            value = value_row.locator(
                self._selectors.VALUE_COLUMN.replace(
                    "##value##", "ind_base_achieved_val"
                )
            ).text_content()
            year = value_row.locator(
                self._selectors.YEAR_COLUMN.replace("##year##", "latestYear")
            ).text_content()
            table_data[left_column_cell_value] = {year: value}
        return table_data
