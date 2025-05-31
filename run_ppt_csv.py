import sys
import os
from create_ppt_csv import create_ppt_csv
import tkinter as tk
from tkinter import filedialog
"""
This script converts a CSV file into a PowerPoint presentation.
Usage:
    python run_ppt_csv.py <openaikey_txt> <input_csv> <output_pptx>
Arguments:
    <openaikey_txt> Path to the text file containing the OpenAI API key.
    <input_csv>     Path to the input CSV file.
    <output_pptx>   Path to the output PowerPoint file.
Example:
    python run_ppt_csv.py openai_key.txt input_sample.csv output_csv.pptx
"""

def main():
    def get_file_path(prompt, filetypes):
        root = tk.Tk()
        root.withdraw()  # Hide the main tkinter window
        return filedialog.askopenfilename(title=prompt, filetypes=filetypes)

    def get_save_file_path(prompt, default_extension, filetypes):
        root = tk.Tk()
        root.withdraw()  # Hide the main tkinter window
        return filedialog.asksaveasfilename(title=prompt, defaultextension=default_extension, filetypes=filetypes)

    if len(sys.argv) == 3:
        input_csv = sys.argv[1]
        output_pptx = sys.argv[2]
    else:
        print("Command-line arguments not provided. Opening file dialogs...")
        input_csv = get_file_path("Select the input CSV file", [("CSV files", "*.csv")])
        output_pptx = get_save_file_path("Select the output PowerPoint file", ".pptx", [("PowerPoint files", "*.pptx")])

    create_ppt_csv(input_csv, output_pptx)

if __name__ == "__main__":
    main()