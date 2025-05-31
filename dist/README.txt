# Logos PPT Sermon Translate

## Description
This program generates a PowerPoint file based on input data and uses OpenAI's API for processing.

## Prerequisites
Ensure you have the following files in the same directory as the executable:
- `openaikey.txt`: This file should contain your OpenAI API key.
- `input_sample.txt`: This file should contain the input data for the program.

### For CSV input:
1. Place your CSV file in the same directory as the executable.
2. Run the following command:
    ```
    run_ppt_csv.exe ./openaikey.txt ../samples/input_sample.csv ./output.pptx
    ```

### For TXT input:
1. Place your input file for TXT in the same directory as the executable.
2. Run the following command:
    ```
    run_ppt_llm.exe ./openaikey.txt ../samples/input_sample.txt ./output.pptx
    ```