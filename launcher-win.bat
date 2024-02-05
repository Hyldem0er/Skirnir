@echo off



rem Parameters
set VENV_PYTHON_PATH=".\env\Scripts\python.exe"

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
python --version > nul 2>&1
if %errorLevel% EQU 0 (
    echo Python is already installed.
) else (
    echo Python is not installed. Installing Python...

    rem Installation of python/pip
    curl -o python-installer.exe https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python-installer.exe
    echo Python has been installed.
)

echo "Passe par la"
:: Create python virtualenv
python -m venv env

echo "Passe par ici"

:: Activate the environement
.\env\Scripts\activate

echo "Passons ensemble"
:: Install pip packages (use python exec path in the virtualenv)
%VENV_PYTHON_PATH% -m pip install -r requirements.txt

echo "Final"
:: Start main program
%VENV_PYTHON_PATH% main.py --ui

exit