# Deploy to Railway - Step by Step Guide

## 🚂 Railway Deployment Instructions

### Step 1: Prepare Your Code

✅ Already done! Your project is ready for deployment.

### Step 2: Create Railway Account

1. Go to **https://railway.app**
2. Sign up with GitHub (recommended) or email
3. Verify your account

### Step 3: Create New Project

1. Click **"New Project"**
2. Choose **"Deploy from GitHub repo"**
3. If this is your first time:
   - Click **"Configure GitHub App"**
   - Select your repository
   - Grant Railway access

### Step 4: Select Your Repository

1. Choose your Django project repository
2. Railway will auto-detect it's a Python/Django project
3. Click **"Deploy Now"**

### Step 5: Configure Environment Variables

In your Railway project dashboard:

1. Click on your service
2. Go to **"Variables"** tab
3. Click **"+ New Variable"** and add:

```
SECRET_KEY=<your-generated-secret-key>
DEBUG=False
ALLOWED_HOSTS=${{ RAILWAY_PUBLIC_DOMAIN }}
CSRF_TRUSTED_ORIGINS=https://${{ RAILWAY_PUBLIC_DOMAIN }}
PYTHON_VERSION=3.13.8
```

**Railway automatically provides `RAILWAY_PUBLIC_DOMAIN` variable!**

### Step 6: Configure Build & Start Commands

Railway usually auto-detects, but to be sure:

1. Go to **"Settings"** tab
2. Set **Build Command**: 
   ```
   pip install -r requirements.txt && cd myapp && python manage.py collectstatic --no-input && python manage.py migrate
   ```
3. Set **Start Command**:
   ```
   cd myapp && gunicorn myapp.wsgi:application
   ```

### Step 7: Deploy!

1. Railway will automatically deploy when you push to GitHub
2. Wait for the build to complete (2-3 minutes)
3. Once deployed, click **"View Logs"** to monitor
4. Your app will be available at: `https://your-app.up.railway.app`

### Step 8: Generate Domain

1. Go to **"Settings"** → **"Networking"**
2. Click **"Generate Domain"**
3. Railway will provide a free `.up.railway.app` subdomain

### Step 9: Update Environment Variables with Your Domain

Once you have your Railway domain:

1. Go back to **"Variables"**
2. Update these (Railway does this automatically if you used `${{ RAILWAY_PUBLIC_DOMAIN }}`):
   - `ALLOWED_HOSTS=your-app.up.railway.app`
   - `CSRF_TRUSTED_ORIGINS=https://your-app.up.railway.app`

### Step 10: Create Superuser (Optional)

To access Django admin:

1. Go to your Railway project
2. Click on your service → **"Settings"**
3. Scroll to **"Networking"** 
4. Under **"One-Click Deploy"**, you can add a custom start command temporarily

Or use Railway CLI:
```bash
railway run python myapp/manage.py createsuperuser
```

## 🔥 Firebase Configuration

For Firebase credentials in Railway:

**Method 1: Environment Variable (Recommended)**
1. Copy content of `serviceAccountKey.json`
2. In Railway Variables, add:
   ```
   FIREBASE_CREDENTIALS=<paste entire JSON here>
   ```
3. Update your Django code to read from environment variable

**Method 2: Upload File**
- Not recommended as Railway uses ephemeral storage

## 📦 Railway Features

- **Automatic Deployments**: Push to GitHub = auto-deploy
- **Free Tier**: $5 credit monthly (enough for small projects)
- **Easy Logs**: Real-time logs in dashboard
- **Custom Domains**: Add your own domain easily
- **Database Add-ons**: Easy to add PostgreSQL if needed

## 🐛 Troubleshooting

### Build Fails?
- Check **"Build Logs"** in Railway dashboard
- Verify `requirements.txt` has all dependencies
- Make sure Python version matches

### App Crashes?
- Check **"Deploy Logs"**
- Common issues:
  - Missing environment variables
  - Database migration errors
  - Static files not collected

### Can't Access Admin?
- Make sure you've created a superuser
- Check ALLOWED_HOSTS includes your Railway domain

## 🔄 Updating Your App

1. Make changes locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update description"
   git push
   ```
3. Railway auto-deploys! ✨

## 💡 Pro Tips

1. **PostgreSQL**: Add Railway PostgreSQL for production
   - In Railway: Click "+ New" → "Database" → "PostgreSQL"
   - Railway auto-adds `DATABASE_URL` variable
   - Update Django settings to use it

2. **Environment Variables**: Use Railway's `${{ VARIABLE }}` syntax

3. **Monitoring**: Enable Railway's monitoring for uptime tracking

4. **Logs**: Always check logs if something goes wrong

## 🎉 Your App is Live!

Once deployed, visit: `https://your-app.up.railway.app`

Need help? Check Railway docs: https://docs.railway.app
