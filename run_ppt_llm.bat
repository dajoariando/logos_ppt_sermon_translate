@echo off
REM Example function invocation
REM run_ppt_llm.bat input_sample.txt output_llm.pptx

REM Create a virtual environment
python -m venv .venv

REM Activate the virtual environment
call .venv\Scripts\activate.bat

REM Install required Python packages
pip install -r requirements.txt -q

REM Check if the correct number of arguments are provided
IF "%~2"=="" (
    echo Usage: %~nx0 ^<input_file^> ^<output_file^>
    exit /b 1
)

REM Assign arguments to variables
set INPUT_FILE=%1
set OUTPUT_FILE=%2

REM Connect with OPENAI API
IF NOT EXIST openaikey.txt (
    echo Error: openaikey.txt does not exist. Get OpenAI API key from OpenAI website and save it in openaikey.txt
    exit /b 1
)
set /p OPENAI_API_KEY=<openaikey.txt

REM Run the Python script with the specified input and output files
python -u run_ppt_llm.py "%INPUT_FILE%" "%OUTPUT_FILE%"
