# Setup
```sh
sudo apt install python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Verify installation
```sh
pip list
```

## Connect with OpenAI API
```sh
export OPENAI_API_KEY=$(cat openaikey.txt)
echo $OPENAI_API_KEY
```

## Run scripts
You can run `create_ppt_csv.py` or `create_ppt_llm.py` from within VSCode, or run this code from the shell:
```sh
./run_ppt_llm.sh input_sample.txt output_llm.pptx
./run_ppt_csv.sh input_sample.csv output_csv.pptx
./run_ppt_csv.bat input_sample.csv output_csv.pptx
```
Or you can run precompiled binary from dist folder in Windows:
```
run_ppt_llm.exe input_sample.txt output_llm.pptx
```

## Clean up
To deactivate the virtual environment:
```sh
deactivate
```

## Create standalone application (tested in Windows)
pip install pyinstaller
pyinstaller --onefile run_ppt_llm.py