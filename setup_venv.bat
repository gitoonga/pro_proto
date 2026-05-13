@echo off
REM setup_venv.bat
REM This script sets up a Python virtual environment for the project using CMD.

set VENV_DIR=.venv

REM 1. Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in your PATH. Please install Python 3.x.
    exit /b 1
)

REM 2. Create virtual environment if it doesn't exist
if not exist %VENV_DIR% (
    echo Creating virtual environment in '%VENV_DIR%'...
    python -m venv %VENV_DIR%
    if %errorlevel% neq 0 (
        echo Failed to create virtual environment.
        exit /b 1
    )
) else (
    echo Virtual environment '%VENV_DIR%' already exists.
)

REM 3. Upgrade pip and install requirements
echo Installing/Updating requirements...
%VENV_DIR%\Scripts\python.exe -m pip install --upgrade pip
if exist requirements.txt (
    %VENV_DIR%\Scripts\python.exe -m pip install -r requirements.txt
) else (
    echo No requirements.txt found. Installing basic 'protobuf' library...
    %VENV_DIR%\Scripts\python.exe -m pip install protobuf
)

echo.
echo Setup complete!
echo To activate the virtual environment, run:
echo %VENV_DIR%\Scripts\activate.bat
