#!/bin/bash

## abort on nonzero exitstatus
set -o errexit
## abort on unbound variable
set -o nounset

####################################################
#                    Parameters
####################################################

VENV_PYTHON_PATH=${VENV_PYTHON_PATH:-./env/bin/python}

####################################################
#              Function declaration
####################################################

is_debian() {
## check if os is debian
    if [ -f /etc/debian_version ]; then
        return 0
    else
        return 1
    fi
}

install_app_dependencies() {
## install pip packages
    sudo apt -y install python3 \
        python3.11-venv \
        python3-pip \

    if is_debian; then
        sudo apt -y install libgl1-mesa-glx
    fi
}

####################################################
#              Main function logic
####################################################

install_app_dependencies

## Create python virtualenv
python3 -m venv env

## Activate the environnement
. env/bin/activate

## Install pip packages (use python exec path in the virtualenv)
${VENV_PYTHON_PATH} -m pip install -r requirements.txt

## Start main programm
${VENV_PYTHON_PATH} main.py --ui