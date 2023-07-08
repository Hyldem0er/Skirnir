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
	pip install -r requirement.txt

# Run the main.py script
run:
	$(PYTHON) main.py

# Delete the virtual environment
clean:
	rm -rf env

# Default target
all: env activate install run
