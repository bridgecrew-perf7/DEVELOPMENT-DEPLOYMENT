# Python3 Ubuntu Debugging

### set main python version

```console
which python
ls /usr/bin/
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/pythonSELECTEDVERSION
```

### Atom + Atom Script + VIM-Module-Plus
update the grammar in  Atom's /script/lib/grammar/python.js
open Atom via Terminal
```console
atom .
```
### Remove and Update repositories
```console
sudo rm /etc/apt/sources.list.d/*
sudo add-apt-repository main
sudo add-apt-repository universe
sudo add-apt-repository restricted
sudo add-apt-repository multiverse
sudo add-apt-repository ppa:ondrej/php
sudo apt-get update
```
### Install new Ubuntu distribution
```console
sudo apt update
sudo apt upgrade
sudo apt dist-upgrade
sudo apt autoremove
sudo do-release-upgrade
```
