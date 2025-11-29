#!/usr/bin/env bash up
echo "Starting build process..."
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
echo "Build completed!"