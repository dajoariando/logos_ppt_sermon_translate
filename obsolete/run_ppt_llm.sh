#!/bin/bash

# Example function invocation
# ./run_ppt_llm.sh input_sample.txt output_llm.pptx

# Install Python virtual environment package
# sudo apt install python3-venv -y

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install required Python packages
pip install -r requirements.txt -q

# Verify installation (optional)
# pip list

# Check if the correct number of arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <input_file> <output_file>"
    exit 1
fi

# Assign arguments to variables
INPUT_FILE=$1
OUTPUT_FILE=$2

# Connect with OPENAI API
if [ ! -f openaikey.txt ]; then
    echo "Error: openaikey.txt does not exist. Get OpenAI API key from OpenAI website and save it in openaikey.txt"
    exit 1
fi
export OPENAI_API_KEY=$(cat openaikey.txt)

# Run the Python script with the specified input and output files
python -u run_ppt_llm.py "$INPUT_FILE" "$OUTPUT_FILE"