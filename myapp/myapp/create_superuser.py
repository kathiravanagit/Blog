"""
Script to create a default superuser if none exists.
Run this after deployment.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Check if superuser already exists
if not User.objects.filter(is_superuser=True).exists():
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'changeme123')
    
    User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print(f'Superuser "{username}" created successfully!')
else:
    print('Superuser already exists.')
