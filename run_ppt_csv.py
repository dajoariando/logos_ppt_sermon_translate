import sys
"""
This script converts a CSV file into a PowerPoint presentation.
Usage:
    python run_ppt_csv.py <input_csv> <output_pptx>
Arguments:
    <input_csv>   Path to the input CSV file.
    <output_pptx> Path to the output PowerPoint file.
Example:
    python run_ppt_csv.py input_sample.csv output_csv.pptx
"""
from create_ppt_csv import create_ppt_csv



def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_csv> <output_pptx>")
        sys.exit(1)
    
    input_csv = sys.argv[1]
    output_pptx = sys.argv[2]
    
    create_ppt_csv(input_csv, output_pptx)

if __name__ == "__main__":
    main()