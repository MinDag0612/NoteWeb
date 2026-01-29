#!/bin/bash
set -e

echo "=== DEPLOY START ==="

# ---- CONFIG ----
PROJECT_DIR=/var/www/NoteWeb
BACKEND_DIR=$PROJECT_DIR/backendSrc
VENV_DIR=$BACKEND_DIR/venv

# ---- FRONTEND ----
echo "Build frontend..."
cd $PROJECT_DIR
npm install
npm run build

# ---- BACKEND ----
echo "Setup backend..."
cd $BACKEND_DIR

if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

$VENV_DIR/bin/pip install -r requirements.txt

echo "=== DEPLOY DONE ==="
