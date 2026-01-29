import os
import firebase_admin
from firebase_admin import credentials, firestore
from django.conf import settings

# Initialize Firebase Admin SDK
def initialize_firebase():
    """Initialize Firebase app if not already initialized."""
    if not firebase_admin._apps:
        # Get the path to the service account key
        cred_path = os.path.join(settings.BASE_DIR, 'myapp', 'serviceAccountKey.json')
        
        # Initialize credentials
        cred = credentials.Certificate(cred_path)
        
        # Initialize the app
        firebase_admin.initialize_app(cred)
        
    return firestore.client()

# Get Firestore database instance
def get_db():
    """Get Firestore database instance."""
    initialize_firebase()
    return firestore.client()
