import sys
import os
from create_ppt_llm import create_ppt_llm
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
    if len(sys.argv) != 4:
        print("Usage: python run_ppt_llm.py <openaikey_txt> <input_txt> <output_pptx>")
        sys.exit(1)
    
    openaikey_txt = sys.argv[1]
    input_txt = sys.argv[2]
    output_pptx = sys.argv[3]

    print(f"Using OpenAI API key from: {openaikey_txt}")

    with open(openaikey_txt, 'r') as file:
        os.environ["OPENAI_API_KEY"] = file.read().strip()
    
    create_ppt_llm(input_txt, output_pptx)

if __name__ == "__main__":
    main()