# Determine the operating system
ifeq ($(OS),Windows_NT)
    DETECTED_OS := Windows
else
    DETECTED_OS := $(shell uname -s)
endif

# Set the Python executable based on the detected operating system
ifeq ($(DETECTED_OS),Windows)
    PYTHON = python
    ACTIVATE = .\env\Scripts\activate
else
    PYTHON = python3
    VENV_PYTHON_BIN= ./env/bin/python
    ACTIVATE = . env/bin/activate
endif

# Create a virtual environment
env:
	$(PYTHON) -m venv env

# Activate the virtual environment based on the detected operating system
activate:
	$(ACTIVATE)

# Install required modules
install:
	$(VENV_PYTHON_BIN) -m pip install -r requirements.txt

# Run the main.py script
run:
	$(VENV_PYTHON_BIN) main.py --ui

# Delete the virtual environment
clean:
	rm -rf env

# Default target
all: env activate install run
