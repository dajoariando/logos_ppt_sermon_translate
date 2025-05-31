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

## Run scripts

To run the provided scripts, use the following commands:

### For `run_ppt_csv.py`
```sh
python run_ppt_csv.py input_sample.csv output.pptx
```

### For `run_ppt_llm.py`
```sh
python run_ppt_llm.py input_sample.txt output.pptx
```

### Run precompiled binary (Windows only)

If you are using Windows, you can run the precompiled binary located in the `dist` folder:

```sh
run_ppt_llm.exe openaikey.txt input_sample.txt output.pptx
```

## Clean up
To deactivate the virtual environment:
```sh
deactivate
```

## Create standalone application (tested in Windows)
pip install pyinstaller
pyinstaller --onefile run_ppt_llm.py