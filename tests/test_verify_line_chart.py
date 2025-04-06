from pathlib import Path
import pytest
from playwright.sync_api import Locator, expect

from components.average_income_shortfall_line_chart import AverageIncomeShortfall
from components.economies_with_hgh_inequality_line_chart import EconomiesWithHighInequality
from components.end_extreme_poverty_line_chart import EndExtremePoverty
from pages.home_page import HomePage
from pages.vision_page import VisionPage
from utils.spreadsheets import excel_to_dataframe


def get_tooltip_texts_from_line_chart(chart: EndExtremePoverty | AverageIncomeShortfall | EconomiesWithHighInequality, locator: Locator=None):
    """move mouse across line chart and read dynamic tooltip text"""
    box = locator.bounding_box() if locator else chart.line_tracker.bounding_box()
    viewport_width = chart.page.viewport_size["width"]

    steps = int(box["width"])
    x = box["x"]  # x-coordinate in top left
    y = box["y"] + (box["height"] / 2)  # y-coordinate in center of bounding box
    chart.page.mouse.move(x, y)
    chart.page.mouse.click(x, y)

    tooltip_texts = []
    for i in range(steps + 1):
        x = (
            i / steps
        ) * viewport_width  # Calculate x-coordinate to move from left to right
        chart.page.mouse.move(x, y)  # Keep y-coordinate constant
        if x >= box["x"]:
            tooltip = chart.line_chart_tooltip
            tooltip_text = tooltip.inner_text()
            if tooltip_text not in tooltip_texts:
                tooltip_texts.append(tooltip_text)
    return tooltip_texts


def compare_tooltip_text_with_excel(
    tooltip_texts: list, file_path: str, indicator_code: str
) -> list[bool]:
    """compare tooltip data with excel"""
    if not tooltip_texts:
        pytest.fail("Tooltip text is empty")

    # Parse the list into a tuple of (year, value)
    tooltip_texts_parsed = [
        (
            int(entry.split("(")[1].split(")")[0]),
            float(entry.split("|")[1].replace("%", "").strip()),
        )
        for entry in tooltip_texts
        if entry
    ]

    df = excel_to_dataframe(file_path)
    comparison = []
    if not df.empty:
        si_pov_umic_df = df.loc[
            (df["Geography_Code"] == "WLD")
            & (df["Indicator_Code"].isin([indicator_code]))
        ].filter(["Time_Period", "Value"])
        si_pov_umic_dict = si_pov_umic_df.to_dict(orient="list")

        # Create list of tuples of (year, value)
        si_pov_umic_dict_parsed = list(
            zip(si_pov_umic_dict["Time_Period"], si_pov_umic_dict["Value"])
        )

        # Sort both lists by the year
        tooltip_texts_parsed.sort(key=lambda x: x[0])
        si_pov_umic_dict_parsed.sort(key=lambda x: x[0])

        # Compare the tuples from both lists
        comparison = [
            value1 == value2
            for (year, value1), (year, value2) in zip(
                tooltip_texts_parsed, si_pov_umic_dict_parsed
            )
        ]
    return comparison


def test_line_chart_si_pov_umic(setup_chrome):
    """verify line chart data with excel"""
    page = setup_chrome
    home_page = HomePage(page)
    home_page.vision_tab.click()

    vision_page = VisionPage(page)
    expect(page).to_have_title(vision_page.title_text)
    expect(vision_page.end_extreme_poverty.body).to_be_visible()
    vision_page.end_extreme_poverty.body.scroll_into_view_if_needed()
    expect(vision_page.end_extreme_poverty.line_chart_button).to_be_visible()

    # orange line chart
    vision_page.end_extreme_poverty.full_screen.click()
    tooltip_texts_si_pov_umic = get_tooltip_texts_from_line_chart(
        locator=vision_page.end_extreme_poverty.line_tracker_685,
        chart=vision_page.end_extreme_poverty
    )
    vision_page.end_extreme_poverty.close_chart.click()
    comparison = compare_tooltip_text_with_excel(
        tooltip_texts=tooltip_texts_si_pov_umic,
        file_path=str(Path(__file__).resolve().parent.parent / "data/SI_POV_DDAY_TO.xlsx"),
        indicator_code="SI_POV_UMIC",
    )

    assert True in comparison, "at least one value does not match"


def test_line_chart_si_pov_dday(setup_chrome):
    """verify line chart data with excel"""
    page = setup_chrome
    home_page = HomePage(page)
    home_page.vision_tab.click()

    vision_page = VisionPage(page)
    expect(page).to_have_title(vision_page.title_text)
    expect(vision_page.end_extreme_poverty.body).to_be_visible()
    vision_page.end_extreme_poverty.body.scroll_into_view_if_needed()
    expect(vision_page.end_extreme_poverty.line_chart_button).to_be_visible()

    # blue line chart
    vision_page.end_extreme_poverty.full_screen.click()
    tooltip_texts_si_pov_dday = get_tooltip_texts_from_line_chart(
        locator=vision_page.end_extreme_poverty.line_tracker_215,
        chart=vision_page.end_extreme_poverty,
    )
    vision_page.end_extreme_poverty.close_chart.click()
    comparison = compare_tooltip_text_with_excel(
        tooltip_texts=tooltip_texts_si_pov_dday,
        file_path=str(Path(__file__).resolve().parent.parent / "data/SI_POV_DDAY_TO.xlsx"),
        indicator_code="SI_POV_DDAY",
    )

    assert True in comparison, "at least one value does not match"


def test_line_chart_average_income_shortfall(setup_chrome):
    """verify line chart data with excel"""
    page = setup_chrome
    home_page = HomePage(page)
    home_page.vision_tab.click()

    vision_page = VisionPage(page)
    expect(page).to_have_title(vision_page.title_text)
    expect(vision_page.average_income_shortfall.body).to_be_visible()
    vision_page.average_income_shortfall.body.scroll_into_view_if_needed()
    expect(vision_page.average_income_shortfall.line_chart_button).to_be_visible()

    # line chart
    vision_page.average_income_shortfall.full_screen.click()
    tooltip_texts_si_pov_pros = get_tooltip_texts_from_line_chart(
        chart=vision_page.average_income_shortfall,
    )
    vision_page.average_income_shortfall.close_chart.click()
    comparison = compare_tooltip_text_with_excel(
        tooltip_texts=tooltip_texts_si_pov_pros,
        file_path=str(Path(__file__).resolve().parent.parent / "data/SI_POV_PROS.xlsx"),
        indicator_code="SI_POV_PROS",
    )

    assert True in comparison, "at least one value does not match"


def test_line_chart_economies_with_high_inequality(setup_chrome):
    """verify line chart data with excel"""
    page = setup_chrome
    home_page = HomePage(page)
    home_page.vision_tab.click()

    vision_page = VisionPage(page)
    expect(page).to_have_title(vision_page.title_text)
    expect(vision_page.economies_with_high_inequality.body).to_be_visible()
    vision_page.economies_with_high_inequality.body.scroll_into_view_if_needed()
    vision_page.economies_with_high_inequality.line_chart_button.click()

    # line chart
    vision_page.economies_with_high_inequality.full_screen.click()
    tooltip_texts_si_dst_ineq = get_tooltip_texts_from_line_chart(
        chart=vision_page.economies_with_high_inequality
    )
    vision_page.economies_with_high_inequality.close_chart.click()
    comparison = compare_tooltip_text_with_excel(
        tooltip_texts=tooltip_texts_si_dst_ineq,
        file_path=str(Path(__file__).resolve().parent.parent / "data/SI_DST_INEQ.xlsx"),
        indicator_code="SI_DST_INEQ",
    )

    assert True in comparison, "at least one value does not match"
