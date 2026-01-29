#!/usr/bin/env python
"""
Quick script to check Firebase connection status
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
django.setup()

from myapp.firebase_config import get_db

def check_connection():
    try:
        db = get_db()
        print("✅ Firebase connection successful!")
        print(f"   Database type: {type(db).__name__}")
        
        # Try to list collections
        collections = list(db.collections())
        print(f"✅ Collections found: {len(collections)}")
        for col in collections:
            count = len(list(col.stream()))
            print(f"   - {col.id}: {count} document(s)")
        
        return True
    except Exception as e:
        print(f"❌ Firebase connection failed: {e}")
        return False

if __name__ == "__main__":
    check_connection()
