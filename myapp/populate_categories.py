#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
django.setup()

from blog.models import Category
from myapp.firebase_config import get_db

# Get all unique categories from Firebase posts
db = get_db()
posts_ref = db.collection('posts').stream()

categories_set = set()
for doc in posts_ref:
    post_data = doc.to_dict()
    if 'category' in post_data:
        categories_set.add(post_data['category'])

# Add categories to Django database
for category_name in categories_set:
    category, created = Category.objects.get_or_create(
        name=category_name,
        defaults={'description': f'{category_name} posts'}
    )
    if created:
        print(f"✓ Added category: {category_name}")
    else:
        print(f"✗ Category already exists: {category_name}")

print(f"\nTotal categories: {len(categories_set)}")
print("Done! Categories are now available in the admin panel.")
