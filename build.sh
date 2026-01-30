#!/usr/bin/env bash
# Build script for deployment - Updated Jan 30, 2026

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

# Create superuser if environment variables are set
if [ -n "$DJANGO_SUPERUSER_USERNAME" ]; then
    python ../myapp/create_superuser.py
fi
