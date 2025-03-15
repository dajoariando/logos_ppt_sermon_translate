import sys
from create_ppt_llm import create_ppt_llm
"""
This script converts a text file into a PowerPoint presentation.
Usage:
    python run_ppt_llm.py <input_txt> <output_pptx>
Arguments:
    <input_txt>   Path to the input text file.
    <output_pptx> Path to the output PowerPoint file.
Example:
    python run_ppt_llm.py 250315_input_english.txt output_llm.pptx
"""
def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_csv> <output_pptx>")
        sys.exit(1)
    
    input_csv = sys.argv[1]
    output_pptx = sys.argv[2]
    
    create_ppt_llm(input_csv, output_pptx)

if __name__ == "__main__":
    main()