#!/usr/bin/env bash

echo "Installing MongoDB"
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
sudo apt-get update
sudo apt-get install -y mongodb-org

echo "Install Python PIP"
apt-get -y install python-pip python-dev build-essential

echo "Install Virtualenv"
pip install virtualenv

echo "Install Flask"
pip install flask

echo "Install Pymongo"
pip install pymongo
