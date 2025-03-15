#!/bin/bash

# Example function invocation
# ./run_ppt_csv.sh input_english_indo.csv output_csv.pptx

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

# Run the Python script with the specified input and output files
python run_ppt_csv.py "$INPUT_FILE" "$OUTPUT_FILE"