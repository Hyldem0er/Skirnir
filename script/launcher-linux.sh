#!/bin/bash

sudo apt -y install python3
sudo apt -y install make
sudo apt -y install python3.11-venv
sudo apt -y install python3-pip
make all

echo "#!/bin/bash

make run" > launcher.sh