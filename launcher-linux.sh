#!/bin/bash

is_debian() {
    if [ -f /etc/debian_version ]; then
        return 0
    else
        return 1
    fi
}

sudo apt -y install python3
sudo apt -y install make
sudo apt -y install python3.11-venv
sudo apt -y install python3-pip

if is_debian; then
    sudo apt -y install libgl1-mesa-glx
fi

make all

echo "#!/bin/bash
make run" > launcher-linux.sh