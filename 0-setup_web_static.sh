#!/usr/bin/env bash
# This script sets up the web servers for deployment

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "Hello World!" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '30i\\tlocation /hbtn_static/ {\n\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
