@echo off

rem Parameters
set VENV_PYTHON_PATH=".\\env\\Scripts\\python.exe"

:: echo %VENV_PYTHON_PATH%

rem Check if the script is running with administrator privileges
net session >nul 2>&1
if %errorLevel% NEQ 0 (
    echo The first time this script must be run with administrator privileges.
    echo To run this script as an administrator, right-click and select "Run as administrator."
    pause
    exit /b 1
)

rem Check if Python is already installed
%VENV_PYTHON_PATH% --version > nul 2>&1
if %errorLevel% EQU 0 (
    echo Python is already installed.
) else (
    echo Python is not installed. Installing Python...

    rem Download Python installer
    :: You can download the Python installer manually and include it in your script
    :: or use a tool like curl if it's available on your system
    echo Please download Python installer manually and rerun this script.
    pause
    exit /b 1
)

:: Create python virtualenv
%VENV_PYTHON_PATH% -m venv env

:: Activate the environment
call .\env\Scripts\activate

:: Install pip packages (use python exec path in the virtualenv)
%VENV_PYTHON_PATH% -m pip install -r requirements.txt

:: Start main program
%VENV_PYTHON_PATH% main.py --ui

exit
