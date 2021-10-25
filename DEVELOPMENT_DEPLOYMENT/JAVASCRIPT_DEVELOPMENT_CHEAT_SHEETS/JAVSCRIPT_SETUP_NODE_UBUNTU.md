# Javascript Setup Node on Ubuntu 21.4

Remove and update repositories
```console
sudo rm /etc/apt/sources.list.d/*
sudo add-apt-repository main
sudo add-apt-repository universe
sudo add-apt-repository restricted
sudo add-apt-repository multiverse
sudo add-apt-repository ppa:ondrej/php
sudo apt-get update
```

Install Node Version Manager (NVM)
```console
sudo apt install curl
sudo curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
source ~/.bashrc
nvm --version
nvm ls
nvm ls-remote
nvm install 16
```
get node binaries
```console
sudo wget https://nodejs.org/dist/v14.17.0/node-v14.17.0-linux-x64.tar.xz
sudo apt-get install xz-utils
sudo tar -C /usr/local --strip-components 1 -xJf node-v14.17.0-linux-x64.tar.xz
```
