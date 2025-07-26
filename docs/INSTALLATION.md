# Installation Guide

This guide will help you install and set up the Django ChatterBot project on your computer.

## 📋 Prerequisites

Before starting, make sure you have:

- **Python 3.9 or higher** installed on your computer
- **pip** (Python package manager) - usually comes with Python
- **Git** (optional, for cloning the repository)
- Basic knowledge of using terminal/command line

### Check Your Python Version

Open your terminal and run:
```bash
python --version
# or
python3 --version
```

You should see something like `Python 3.9.0` or higher.

### Check pip Installation

```bash
pip --version
# or
pip3 --version
```

## 🚀 Step-by-Step Installation

### Step 1: Download the Project

**Option A: Clone from GitHub (if available)**
```bash
git clone https://github.com/yourusername/django-chatterbot-project.git
cd django-chatterbot-project
```

**Option B: Download and Extract**
1. Download the project files as a ZIP
2. Extract to a folder called `django-chatterbot-project`
3. Open terminal in that folder

### Step 2: Create a Virtual Environment (Recommended)

A virtual environment keeps your project dependencies separate from other Python projects.

```bash
# Create virtual environment
python -m venv chatbot_env

# Activate virtual environment
# On Windows:
chatbot_env\Scripts\activate

# On macOS/Linux:
source chatbot_env/bin/activate
```

You should see `(chatbot_env)` at the beginning of your terminal prompt.

### Step 3: Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt
```

If you don't have the requirements.txt file, install manually:
```bash
pip install django>=4.2.0
pip install chatterbot==1.2.7
pip install chatterbot-corpus>=1.2.0
pip install pytz>=2023.3
```

### Step 4: Set Up Django Database

```bash
# Create database migrations
python manage.py makemigrations

# Apply migrations to create database
python manage.py migrate
```

### Step 5: Create Superuser (Optional)

If you want to access the Django admin panel:
```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### Step 6: Test the Installation

**Test the Web Interface:**
```bash
python manage.py runserver
```

Open your web browser and go to: `http://127.0.0.1:8000/`

**Test the Terminal Interface:**
Open a new terminal (keep the server running) and run:
```bash
python terminal_chatbot.py
```

## 🔧 Troubleshooting

### Common Installation Issues

#### Issue: "pip install chatterbot" fails

**Solution 1:** Try installing dependencies first
```bash
pip install setuptools wheel
pip install chatterbot==1.2.7
```

**Solution 2:** Use different Python version
```bash
# Try with Python 3.9 or 3.10
python3.9 -m pip install chatterbot==1.2.7
```

#### Issue: "No module named django"

**Solution:** Make sure you're in the virtual environment and Django is installed
```bash
# Activate virtual environment first
source chatbot_env/bin/activate  # macOS/Linux
# or
chatbot_env\Scripts\activate     # Windows

# Then install Django
pip install django
```

#### Issue: Database errors

**Solution:** Delete database files and recreate
```bash
# Delete existing database
rm db.sqlite3
rm chatbot_database.sqlite3
rm terminal_bot.sqlite3

# Recreate database
python manage.py makemigrations
python manage.py migrate
```

#### Issue: Port already in use

**Solution:** Use a different port
```bash
python manage.py runserver 8001
```

#### Issue: Import errors with ChatterBot

**Solution:** Try downgrading Python or using specific versions
```bash
pip install chatterbot==1.2.7 --force-reinstall
```

### Verification Steps

After installation, verify everything works:

1. **Check Django:**
   ```bash
   python manage.py check
   ```

2. **Check ChatterBot:**
   ```bash
   python -c "from chatterbot import ChatBot; print('ChatterBot installed successfully')"
   ```

## 🌐 Development vs Production

### For Development (Learning/Testing)
- Use SQLite database (default)
- DEBUG = True in settings.py
- Use Django development server

### For Production (Real Website)
- Use PostgreSQL or MySQL database
- DEBUG = False in settings.py
- Use proper web server (Apache, Nginx)
- Set proper SECRET_KEY
- Configure static files serving

## 📦 Package Versions

This project is tested with:
- Python 3.9+
- Django 4.2+
- ChatterBot 1.2.7
- chatterbot-corpus 1.2.0+

## 🔄 Updating the Project

To update dependencies:
```bash
pip install --upgrade -r requirements.txt
```

To update the database after code changes:
```bash
python manage.py makemigrations
python manage.py migrate
```

## 🧹 Uninstalling

To remove the project:

1. **Deactivate virtual environment:**
   ```bash
   deactivate
   ```

2. **Delete project folder:**
   ```bash
   rm -rf django-chatterbot-project  # macOS/Linux
   rmdir /s django-chatterbot-project  # Windows
   ```

3. **Remove virtual environment:**
   ```bash
   rm -rf chatbot_env  # macOS/Linux
   rmdir /s chatbot_env  # Windows
   ```