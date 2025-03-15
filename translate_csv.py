import pandas as pd
import os

def translate_csv(filename):
    """
    Reads a CSV file, processes its contents, and returns two lists: one for text and one for notes.
    Args:
        filename (str): The path to the CSV file to be read.
    Returns:
        tuple: A tuple containing two lists:
            - text (list): A list of text entries from the first column of the CSV file.
            - notes (list): A list of note entries from the second column of the CSV file.
    Raises:
        FileNotFoundError: If the specified file does not exist.
        pd.errors.EmptyDataError: If the CSV file is empty.
        pd.errors.ParserError: If the CSV file contains parsing errors.
    """
    

    # Read the CSV file
    df = pd.read_csv(filename, encoding="Windows-1252")
    # df = pd.read_csv(filename, encoding="ISO-8859-1")
    # Ensure the file is in the correct path

    # Assign columns to variables
    text_eng = df.iloc[:, 0]  # First column
    text_indo = df.iloc[:, 1]  # Second column

    # drop NaN values
    text_indo = text_indo.dropna()
    text_eng = text_eng.dropna()

    # Convert pandas Series to Python lists
    text_indo = text_indo.tolist()
    text_eng = text_eng.tolist()

    return text_indo, text_eng