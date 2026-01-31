#!/bin/bash
set -e

echo "=== DEPLOY START ==="

# ---- CONFIG ----
PROJECT_DIR=/var/www/NoteWeb
BACKEND_DIR=$PROJECT_DIR/backendSrc
VENV_DIR=$BACKEND_DIR/venv

echo "ReactJS - front-end was built on local"

echo "Please make sure you install NodeJS before."

echo "Install virtual enviroment run backend python"
sudo apt update
sudo apt install -y python3-venv python3-pip

# ---- BACKEND ----
echo "Setup backend..."
cd $BACKEND_DIR

Lệnh tạo venv
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

# Cái dependence
$VENV_DIR/bin/pip install --upgrade pip
$VENV_DIR/bin/pip install -r requirements.txt


echo "=== DEPLOY DONE ==="

echo "=== NEXT STEP: config .env; nginx, systemd run python venv"

echo "config NginX and"
