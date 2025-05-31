# Setup

### For Linux/MacOS
```sh
sudo apt install python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### For Windows
```sh
python -m venv .venv
.venv\Scripts\activate
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
.\dist\run_ppt_csv.exe ./openaikey.txt ../samples/input_sample.csv ./output.pptx
.\dist\run_ppt_llm.exe ./openaikey.txt ../samples/input_sample.txt ./output.pptx
```

## Clean up
To deactivate the virtual environment:

### For Linux/MacOS
```sh
deactivate
```

### For Windows
```sh
.venv\Scripts\deactivate
```

## Create standalone application (tested in Windows)
```sh
pyinstaller --onefile run_ppt_llm.py
```