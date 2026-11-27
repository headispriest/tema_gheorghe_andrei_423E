@echo off
if not exist venv (
    echo Setting up environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate.bat
)
pytest 1
pause