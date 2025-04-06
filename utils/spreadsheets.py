import pandas as pd
from pandas import DataFrame


def excel_to_dataframe(file_path, sheet_name=0) -> DataFrame | None:
    """
    Converts an Excel sheet to a dataframe.

    Args:
        file_path (str): Path to the Excel file.
        sheet_name (str or int, optional): Name or index of the sheet to read. Defaults to 0 (first sheet).
        orient (str, optional): Determines the structure of the output dictionary.
            Options include 'dict', 'list', 'series', 'split', 'records', 'index'. Defaults to 'dict'.

    Returns:
        dict: A dictionary representation of the Excel sheet.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return df
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
