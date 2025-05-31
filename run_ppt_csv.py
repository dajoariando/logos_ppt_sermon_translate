import sys
import os
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
from create_ppt_csv import create_ppt_csv



def main():
    if len(sys.argv) != 4:
        print("Usage: python run_ppt_csv.py <openaikey_txt> <input_csv> <output_pptx>")
        sys.exit(1)
    
    openaikey_txt = sys.argv[1]
    input_csv = sys.argv[2]
    output_pptx = sys.argv[3]

    print(f"Using OpenAI API key from: {openaikey_txt}")

    with open(openaikey_txt, 'r') as file:
        os.environ["OPENAI_API_KEY"] = file.read().strip()
    
    create_ppt_csv(input_csv, output_pptx)

if __name__ == "__main__":
    main()