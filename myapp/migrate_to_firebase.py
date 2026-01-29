"""
Script to migrate all local SQLite data to Firebase
Run this script once to transfer existing data to Firebase
"""
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
django.setup()

from blog.models import AboutUs, Category, Post
from myapp.firebase_config import get_db
from google.cloud import firestore

def migrate_aboutus():
    """Migrate About Us content to Firebase"""
    print("Migrating About Us data...")
    db = get_db()
    about_us = AboutUs.objects.first()
    
    if about_us:
        db.collection('aboutus').document('content').set({
            'content': about_us.content,
            'updated_at': firestore.SERVER_TIMESTAMP
        })
        print(f"✓ About Us content migrated successfully")
    else:
        print("⚠ No About Us content found in SQLite")

def migrate_categories():
    """Migrate all categories to Firebase"""
    print("\nMigrating Categories...")
    db = get_db()
    categories = Category.objects.all()
    
    count = 0
    for category in categories:
        db.collection('categories').document(str(category.id)).set({
            'name': category.name,
            'description': category.description,
            'created_at': category.created_at.isoformat() if category.created_at else None
        })
        count += 1
        print(f"✓ Migrated category: {category.name}")
    
    print(f"✓ Total {count} categories migrated")

def migrate_posts():
    """Migrate all posts to Firebase"""
    print("\nMigrating Posts...")
    db = get_db()
    posts = Post.objects.all()
    
    count = 0
    for post in posts:
        db.collection('posts').document(str(post.id)).set({
            'title': post.title,
            'slug': post.slug,
            'author': post.author,
            'category_id': str(post.category.id),
            'category_name': post.category.name,
            'content': post.content,
            'image_url': post.image_url,
            'published': post.published,
            'created_at': post.created_at.isoformat() if post.created_at else None,
            'updated_at': post.updated_at.isoformat() if post.updated_at else None
        })
        count += 1
        print(f"✓ Migrated post: {post.title}")
    
    print(f"✓ Total {count} posts migrated")

def main():
    print("=" * 60)
    print("SQLITE TO FIREBASE MIGRATION")
    print("=" * 60)
    
    try:
        migrate_aboutus()
        migrate_categories()
        migrate_posts()
        
        print("\n" + "=" * 60)
        print("✓ MIGRATION COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        print("\nAll data has been migrated to Firebase.")
        print("Your data is now safe in the cloud and accessible from anywhere.")
        
    except Exception as e:
        print(f"\n✗ Migration failed: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
