from pathlib import Path

from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.indicator_detail_SI_DST_INEQ_page import IndicatorDetail_SI_DST_INEQ
from pages.indicator_detail_SI_POV_DDAY_TO_page import IndicatorDetail_SI_POV_DDAY_TO
from pages.indicator_detail_SI_POV_PROS_page import IndicatorDetail_SI_POV_PROS
from pages.vision_page import VisionPage
from utils.spreadsheets import excel_to_dataframe


def compare_table_data_with_excel(
    table_data: dict, file_path: str, indicator_code: str
):
    """compare table data with Excel"""
    df = excel_to_dataframe(file_path)

    if not df.empty:
        si_pov_pros_df = df.filter(
            ["Geography_Name", "Indicator_Code", "Time_Period", "Value"]
        )
        for k, v in table_data.items():
            year = list(v.keys())[0]
            country_df = si_pov_pros_df.loc[
                (si_pov_pros_df["Geography_Name"] == k)
                & (si_pov_pros_df["Time_Period"].astype(str).str.contains(year))
            ]
            si_pov_pros_percentage = int(v[year])

            expected_value = int(country_df.filter(["Value"]).values[0])
            assert (
                si_pov_pros_percentage == expected_value
            ), f"value for  country {k}, year {year}, indicator code {indicator_code} is not matching"


def test_verify_vision_indicator_detail_si_pov_dday(setup_chrome):
    page = setup_chrome
    home_page = HomePage(page)
    home_page.vision_tab.click()

    vision_page = VisionPage(page)
    expect(page).to_have_title(vision_page.title_text)
    expect(vision_page.end_extreme_poverty.body).to_be_visible()
    vision_page.end_extreme_poverty.body.scroll_into_view_if_needed()
    vision_page.end_extreme_poverty.more_data.click()

    indicator_detail_page = IndicatorDetail_SI_POV_DDAY_TO(page)
    expect(page).to_have_title(indicator_detail_page.title_text)

    indicator_detail_page.table.wait_for()
    indicator_detail_page.table.scroll_into_view_if_needed()

    table_data = indicator_detail_page.get_table_data()

    file_path = str(
        Path(__file__).resolve().parent.parent / "data/API_SI_POV_DDAY_TO_en_excel.xlsx"
    )
    df = excel_to_dataframe(file_path)

    if not df.empty:
        si_pov_umic_df = df.filter(
            ["Geography_Name", "Indicator_Code", "Time_Period", "Value"]
        )
        for k, v in table_data.items():
            year = list(v.keys())[0]
            country_df = si_pov_umic_df.loc[
                (si_pov_umic_df["Geography_Name"] == k)
                & (si_pov_umic_df["Time_Period"].astype(str).str.contains(year))
            ]
            si_pov_dday_percentage = int(v[year][0].replace("%", "").strip())

            expected_value = int(
                country_df.loc[country_df["Indicator_Code"] == "SI_POV_DDAY"]
                .filter(["Value"])
                .values[0]
            )
            assert (
                si_pov_dday_percentage == expected_value
            ), f"value for  country {k}, year {year}, indicator code SI_POV_DDAY is not matching"
            si_pov_umic_percentage = int(v[year][1].replace("%", "").strip())
            expected_value = int(
                country_df.loc[country_df["Indicator_Code"] == "SI_POV_UMIC"]
                .filter(["Value"])
                .values[0]
            )
            assert (
                si_pov_umic_percentage == expected_value
            ), f"value for  country {k}, year {year}, indictor code SI_POV_UMIC is not matching"


def test_verify_vision_indicator_detail_si_pov_pros(setup_chrome):
    page = setup_chrome
    home_page = HomePage(page)
    home_page.vision_tab.click()

    vision_page = VisionPage(page)
    expect(page).to_have_title(vision_page.title_text)
    expect(vision_page.average_income_shortfall.body).to_be_visible()
    vision_page.average_income_shortfall.body.scroll_into_view_if_needed()
    vision_page.average_income_shortfall.more_data.click()
    indicator_detail_page = IndicatorDetail_SI_POV_PROS(page)
    expect(page).to_have_title(indicator_detail_page.title_text)
    indicator_detail_page.table.wait_for()
    indicator_detail_page.table.scroll_into_view_if_needed()

    table_data = indicator_detail_page.get_table_data()
    compare_table_data_with_excel(
        table_data=table_data,
        file_path=str(
            Path(__file__).resolve().parent.parent
            / "data/API_SI_POV_PROS_en_excel.xlsx"
        ),
        indicator_code="SI_POV_PROS",
    )


def test_verify_vision_indicator_detail_si_dst_ineq(setup_chrome):
    page = setup_chrome
    home_page = HomePage(page)
    home_page.vision_tab.click()

    vision_page = VisionPage(page)
    expect(page).to_have_title(vision_page.title_text)
    expect(vision_page.economies_with_high_inequality.body).to_be_visible()
    vision_page.economies_with_high_inequality.body.scroll_into_view_if_needed()
    vision_page.economies_with_high_inequality.more_data.click()
    indicator_detail_page = IndicatorDetail_SI_DST_INEQ(page)
    expect(page).to_have_title(indicator_detail_page.title_text)
    indicator_detail_page.table.wait_for()
    indicator_detail_page.table.scroll_into_view_if_needed()
    table_data = indicator_detail_page.get_table_data()
    compare_table_data_with_excel(
        table_data=table_data,
        file_path=str(
            Path(__file__).resolve().parent.parent
            / "data/API_SI_DST_INEQ_en_excel.xlsx"
        ),
        indicator_code="SI_DST_INEQ",
    )
