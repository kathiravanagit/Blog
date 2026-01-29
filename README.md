# Django Blog Application

A full-featured blog application built with Django 6.0.1 and Firebase integration for cloud storage and authentication.

## Features

- 📝 Create, read, update, and delete blog posts
- 🏷️ Category management for organizing posts
- 📱 Responsive design with custom CSS
- 🔥 Firebase integration for cloud data storage
- 👤 User authentication and authorization
- 📊 Admin panel for content management
- 💬 About and Contact pages

## Tech Stack

- **Backend**: Django 6.0.1
- **Database**: SQLite3 (local) / Firebase Firestore (cloud)
- **Frontend**: HTML, CSS, JavaScript
- **Cloud Services**: Firebase Admin SDK
- **Python Version**: 3.x

## Project Structure

```
myapp/
├── blog/                      # Main blog application
│   ├── models.py             # Database models (Post, Category, AboutUs)
│   ├── views.py              # View functions
│   ├── urls.py               # URL routing
│   ├── admin.py              # Admin configurations
│   ├── form.py               # Forms
│   ├── templates/            # HTML templates
│   └── static/               # CSS and static files
├── myapp/                    # Project configuration
│   ├── settings.py           # Django settings
│   ├── urls.py               # Main URL configuration
│   ├── firebase_config.py    # Firebase configuration
│   └── serviceAccountKey.json # Firebase credentials (not in repo)
├── manage.py                 # Django management script
├── populate_data.py          # Data seeding script
└── migrate_to_firebase.py    # Firebase migration utility
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Firebase account (for cloud features)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/kathiravanagit/Blog.git
   cd Blog
   ```

2. **Create virtual environment**
   ```bash
   python -m venv env
   ```

3. **Activate virtual environment**
   - Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install django firebase-admin opencv-python numpy
   ```

5. **Firebase Configuration** (Optional)
   - Create a Firebase project at [Firebase Console](https://console.firebase.google.com/)
   - Download your `serviceAccountKey.json`
   - Place it in `myapp/myapp/` directory
   - Update `firebase_config.py` if needed

6. **Run migrations**
   ```bash
   cd myapp
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Populate sample data** (Optional)
   ```bash
   python populate_categories.py
   python populate_data.py
   ```

9. **Run development server**
   ```bash
   python manage.py runserver
   ```

10. **Access the application**
    - Blog: http://127.0.0.1:8000/
    - Admin Panel: http://127.0.0.1:8000/admin/

## Usage

### Creating Blog Posts

1. Log in to the admin panel at `/admin/`
2. Navigate to "Posts" section
3. Click "Add Post" and fill in the details
4. Assign categories and publish

### Managing Categories

Categories help organize blog posts. Create categories from the admin panel before creating posts.

### Firebase Integration

The application supports both SQLite and Firebase Firestore:
- SQLite is used for local development
- Firebase can be enabled for cloud storage
- Use `migrate_to_firebase.py` to migrate data to Firebase


### Firebase Settings

Configure in `myapp/firebase_config.py` with your Firebase credentials.

## Important Files

- `manage.py` - Django management commands
- `populate_data.py` - Seed database with sample data
- `check_firebase.py` - Verify Firebase connection
- `migrate_to_firebase.py` - Migrate data to Firebase

## Security Notes

⚠️ **Important**: The following files are excluded from version control for security:
- `serviceAccountKey.json` - Firebase credentials
- `db.sqlite3` - Local database
- `.env` files - Environment variables
- `__pycache__/` - Python cache files

Never commit sensitive credentials to public repositories!

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
