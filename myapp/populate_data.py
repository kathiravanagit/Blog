#!/usr/bin/env python
"""
Populate Firebase Firestore with sample blog post data
"""
import os
import sys
import django
from datetime import datetime, timedelta
from django.utils.text import slugify

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
django.setup()

from myapp.firebase_config import get_db
from google.cloud.firestore import SERVER_TIMESTAMP

def populate_posts():
    """Add sample blog posts to Firestore"""
    db = get_db()
    
    # Sample blog posts
    posts = [
        {
            'title': 'Getting Started with Django',
            'slug': slugify('Getting Started with Django'),
            'content': 'Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.',
            'author': 'John Doe',
            'category': 'Tutorial',
            'published': True,
            'image_url': 'https://images.unsplash.com/photo-1593720213428-28a5b9e94613?w=800&h=400&fit=crop',
            'created_at': SERVER_TIMESTAMP,
        },
        {
            'title': 'Introduction to Firebase',
            'slug': slugify('Introduction to Firebase'),
            'content': 'Firebase is a platform developed by Google for creating mobile and web applications. It provides a variety of tools and services to help you develop high-quality apps, grow your user base, and earn more money.',
            'author': 'Jane Smith',
            'category': 'Technology',
            'published': True,
            'image_url': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&h=400&fit=crop',
            'created_at': SERVER_TIMESTAMP,
        },
        {
            'title': 'Python Best Practices',
            'slug': slugify('Python Best Practices'),
            'content': 'Writing clean, maintainable Python code is essential for long-term project success. This post covers the most important best practices including PEP 8 style guide, proper documentation, testing strategies, and code organization.',
            'author': 'Alice Johnson',
            'category': 'Programming',
            'published': True,
            'image_url': 'https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=800&h=400&fit=crop',
            'created_at': SERVER_TIMESTAMP,
        },
        {
            'title': 'Building RESTful APIs',
            'slug': slugify('Building RESTful APIs'),
            'content': 'REST (Representational State Transfer) is an architectural style for designing networked applications. Learn how to build robust, scalable RESTful APIs using Django REST Framework with proper authentication and error handling.',
            'author': 'Bob Williams',
            'category': 'Tutorial',
            'published': True,
            'image_url': 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&h=400&fit=crop',
            'created_at': SERVER_TIMESTAMP,
        },
        {
            'title': 'Database Design Principles',
            'slug': slugify('Database Design Principles'),
            'content': 'Good database design is crucial for application performance and maintainability. This article explores normalization, indexing strategies, relationships, and how to design efficient database schemas for your projects.',
            'author': 'John Doe',
            'category': 'Database',
            'published': True,
            'image_url': 'https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=800&h=400&fit=crop',
            'created_at': SERVER_TIMESTAMP,
        },
        {
            'title': 'Cloud Deployment Guide',
            'slug': slugify('Cloud Deployment Guide'),
            'content': 'Deploying your application to the cloud can seem daunting at first. This comprehensive guide walks you through deploying Django applications to various cloud platforms including AWS, Google Cloud, and Azure.',
            'author': 'Sarah Brown',
            'category': 'DevOps',
            'published': False,
            'image_url': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&h=400&fit=crop',
            'created_at': SERVER_TIMESTAMP,
        },
        {
            'title': 'Frontend Frameworks Comparison',
            'slug': slugify('Frontend Frameworks Comparison'),
            'content': 'React, Vue, and Angular are the three most popular frontend frameworks today. This post compares their features, performance, learning curves, and use cases to help you choose the right one for your project.',
            'author': 'Mike Davis',
            'category': 'Web Development',
            'published': True,
            'image_url': 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800&h=400&fit=crop',
            'created_at': SERVER_TIMESTAMP,
        },
        {
            'title': 'Security Best Practices for Web Apps',
            'slug': slugify('Security Best Practices for Web Apps'),
            'content': 'Security should never be an afterthought. Learn about common vulnerabilities like SQL injection, XSS, CSRF, and how to protect your web applications using industry-standard security practices and Django security features.',
            'author': 'Jane Smith',
            'category': 'Security',
            'published': True,
            'image_url': 'https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=800&h=400&fit=crop',
            'created_at': SERVER_TIMESTAMP,
        },
        {
            'title': 'Testing Your Django Application',
            'slug': slugify('Testing Your Django Application'),
            'content': 'Comprehensive testing is essential for maintaining code quality. Discover how to write unit tests, integration tests, and end-to-end tests for your Django applications using pytest and Django test framework.',
            'author': 'Alice Johnson',
            'category': 'Testing',
            'published': True,
            'image_url': 'https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800&h=400&fit=crop',
            'created_at': SERVER_TIMESTAMP,
        },
        {
            'title': 'Understanding Async Programming in Python',
            'slug': slugify('Understanding Async Programming in Python'),
            'content': 'Asynchronous programming allows you to write concurrent code using the async/await syntax. Learn how to leverage async features in Python and Django to build high-performance, scalable applications.',
            'author': 'Bob Williams',
            'category': 'Programming',
            'published': True,
            'image_url': 'https://images.unsplash.com/photo-1515879218367-8466d910aaa4?w=800&h=400&fit=crop',
            'created_at': SERVER_TIMESTAMP,
        },
    ]
    
    print("🔄 Starting to populate Firebase with blog posts...")
    print("-" * 60)
    
    posts_collection = db.collection('posts')
    
    # Add each post to Firebase
    for idx, post in enumerate(posts, 1):
        doc_ref = posts_collection.add(post)
        print(f"✅ Added post {idx}/{len(posts)}: '{post['title']}'")
        print(f"   Document ID: {doc_ref[1].id}")
        print(f"   Author: {post['author']} | Category: {post['category']}")
        print()
    
    print("-" * 60)
    print(f"✅ Successfully added {len(posts)} blog posts to Firebase!")
    print()
    
    # Display summary
    print("📊 Summary:")
    print(f"   Total posts: {len(posts)}")
    print(f"   Published: {sum(1 for p in posts if p['published'])}")
    print(f"   Draft: {sum(1 for p in posts if not p['published'])}")
    print(f"   Categories: {len(set(p['category'] for p in posts))}")
    print(f"   Authors: {len(set(p['author'] for p in posts))}")
    print()
    
    # Verify data
    print("🔍 Verifying data in Firebase...")
    docs = posts_collection.stream()
    count = sum(1 for _ in docs)
    print(f"✅ Verified: {count} documents in 'posts' collection")

def clear_posts():
    """Clear all posts from Firebase (optional cleanup function)"""
    db = get_db()
    posts_collection = db.collection('posts')
    
    docs = posts_collection.stream()
    deleted = 0
    
    for doc in docs:
        doc.reference.delete()
        deleted += 1
    
    print(f"🗑️  Deleted {deleted} posts from Firebase")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--clear':
        print("⚠️  Clearing all posts from Firebase...")
        clear_posts()
    else:
        populate_posts()
        print("\n💡 Tip: Run 'python populate_data.py --clear' to remove all posts")
