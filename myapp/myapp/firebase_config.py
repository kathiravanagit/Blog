import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
from django.conf import settings

# Initialize Firebase Admin SDK
def initialize_firebase():
    """Initialize Firebase app if not already initialized."""
    if not firebase_admin._apps:
        # Try to get credentials from environment variable (for production)
        firebase_creds = os.environ.get('FIREBASE_CREDENTIALS')
        
        if firebase_creds:
            # Parse JSON from environment variable
            cred_dict = json.loads(firebase_creds)
            cred = credentials.Certificate(cred_dict)
        else:
            # Fall back to local file (for development)
            cred_path = os.path.join(settings.BASE_DIR, 'myapp', 'serviceAccountKey.json')
            if os.path.exists(cred_path):
                cred = credentials.Certificate(cred_path)
            else:
                raise FileNotFoundError(
                    "Firebase credentials not found. "
                    "Set FIREBASE_CREDENTIALS environment variable or "
                    "place serviceAccountKey.json in myapp/myapp/"
                )
        
        # Initialize the app
        firebase_admin.initialize_app(cred)
        
    return firestore.client()

# Get Firestore database instance
def get_db():
    """Get Firestore database instance."""
    initialize_firebase()
    return firestore.client()
