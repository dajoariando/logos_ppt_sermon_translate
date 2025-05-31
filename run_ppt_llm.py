import sys
import os
from create_ppt_llm import create_ppt_llm
import tkinter as tk
from tkinter import filedialog
"""
This script converts a text file into a PowerPoint presentation.
Usage:
    python run_ppt_llm.py <openaikey_txt> <input_txt> <output_pptx>
Arguments:
    <openaikey_txt> Path to the text file containing the OpenAI API key.
    <input_txt>     Path to the input text file.
    <output_pptx>   Path to the output PowerPoint file.
Example:
    python run_ppt_llm.py openai_key.txt input_sample.txt output_llm.pptx
"""
def main():

    def get_file_path(prompt):
        root = tk.Tk()
        root.withdraw()  # Hide the main tkinter window
        return filedialog.askopenfilename(title=prompt)

    def get_save_file_path(prompt, default_extension, filetypes):
        root = tk.Tk()
        root.withdraw()  # Hide the main tkinter window
        return filedialog.asksaveasfilename(title=prompt, defaultextension=default_extension, filetypes=filetypes)

    if len(sys.argv) == 4:
        openaikey_txt = sys.argv[1]
        input_txt = sys.argv[2]
        output_pptx = sys.argv[3]
    else:
        print("Command-line arguments not provided. Opening file dialogs...")
        openaikey_txt = get_file_path("Select the OpenAI API key text file")
        input_txt = get_file_path("Select the English text file")
        output_pptx = get_save_file_path("Select the output PowerPoint file", ".pptx", [("PowerPoint files", "*.pptx")])

    with open(openaikey_txt, 'r') as file:
        os.environ["OPENAI_API_KEY"] = file.read().strip()
    
    create_ppt_llm(input_txt, output_pptx)

if __name__ == "__main__":
    main()