#!/usr/bin/bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3
sudo apt-get install libx11-xcb1
sudo apt-get install --reinstall libxcb-xinerama0
sudo apt-get install libmemcached-dev
sudo apt-get install zlib1g-dev
sudo apt-get install whois

sudo apt update
sudo apt upgrade
sudo apt install git
sudo apt install -y unzip xvfb libxi6 libgconf-2-4
sudo apt install python3-pip

pip install -r requirements.txt
pip install selenium
