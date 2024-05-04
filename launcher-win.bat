@echo off

rem Parameters
set VENV_PYTHON_PATH=".\\env\\Scripts\\python.exe"

rem Check if the script is running with administrator privileges
net session >nul 2>&1
if %errorLevel% NEQ 0 (
    echo The first time this script must be run with administrator privileges.
    echo To run this script as an administrator, right-click and select "Run as administrator."
    pause
    exit /b 1
)


REM Check if Python is installed
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Installing...

    REM Download Python installer
    curl -o python-installer.exe https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe
    if not exist python-installer.exe (
        echo Failed to download Python installer.
        goto end
    )

    REM Install Python
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    if %errorlevel% neq 0 (
        echo Failed to install Python.
        goto end
    )

    echo Python installed successfully.
) else (
    echo Python is already installed.
)

:end
endlocal


rem Create python virtualenv
py -3.11 -m venv env

rem Activate the environment
call .\env\Scripts\activate

rem Set the python path variable
set VENV_PYTHON_PATH=".\env\Scripts\python.exe"

rem Install pip packages (use python exec path in the virtualenv)
%VENV_PYTHON_PATH% -m pip install -r requirements.txt

rem Start main program
%VENV_PYTHON_PATH% main.py --ui

exit