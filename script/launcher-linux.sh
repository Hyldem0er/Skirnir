#!/bin/bash

# Fonction pour vérifier si le système est Debian
is_debian() {
    if [ -f /etc/debian_version ]; then
        return 0  # Le système est Debian
    else
        return 1  # Le système n'est pas Debian
    fi
}

# Installation des paquets communs
sudo apt -y install python3
sudo apt -y install make
sudo apt -y install python3.11-venv
sudo apt -y install python3-pip

# Vérification et installation du paquet spécifique pour Debian
if is_debian; then
    sudo apt -y install libgl1-mesa-glx
fi

# Exécution de la commande make all
make all

# Création du script de lancement
echo "#!/bin/bash
make run" > launcher.sh
