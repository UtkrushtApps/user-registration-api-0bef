#!/bin/bash
set -e
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
if command -v docker &> /dev/null
then
    docker-compose build
fi
