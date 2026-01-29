#!/usr/bin/env bash
# Build script for deployment

# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Change to the Django project directory
cd myapp

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate
