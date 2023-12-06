#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static

if ! command -v nginx &> /dev/null
then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/{releases/test,shared}

sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

nginx_config="/etc/nginx/sites-available/default"
sudo sed -i '/location \/static {/!b;n;c\    alias /data/web_static/current/;' $nginx_config

service nginx restart
