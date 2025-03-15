# in the terminal, do these:

sudo apt install python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# verify installation
# pip list

# connect with OPENAI API
export OPENAI_API_KEY=$(cat openaikey.txt)
echo $OPENAI_API_KEY

# and then run create_ppt_csv.py or create_ppt_llm.py from within VSCode.
# or you can run from shell:
#   python run_ppt_llm.py 250315_input_english.txt output_llm.pptx
#   python run_ppt_csv.py input_english_indo.csv output_csv.pptx


# clean up: deactivate venv
# deactivate