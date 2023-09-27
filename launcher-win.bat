@echo off

rem Check if the script is running with administrator privileges
net session >nul 2>&1
if %errorLevel% NEQ 0 (
    echo The first time this script must be run with administrator privileges.
    echo To run this script as an administrator, right-click and select "Run as administrator."
pause
    exit /b 1
)


rem Check if Python is already installed
python --version >nul 2>&1
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


rem Check if Make is already installed
where make >nul 2>&1
if %errorLevel% EQU 0 (
    echo Make is already installed. Skipping Chocolatey and Make installation.
) else (

    rem Installation of Chocolatey with progress display
    @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "(New-Object System.Net.WebClient).DownloadFile('https://chocolatey.org/chocolateyInstall.ps1', 'chocolateyInstall.ps1'); .\chocolateyInstall.ps1" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

    rem Installation of makefile if Make is not already installed
    choco install make -y
)


rem Command make all (install dependencies + run the prosgram)
cd /d "%~dp0"
make all


rem Replace the script with "make run"
echo make run > %~0

exit