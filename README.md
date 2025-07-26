# Django ChatterBot Terminal Client

A simple conversational AI chatbot built with Django and ChatterBot that works both in web browser and terminal.

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [References](#references)

## 🤖 About the Project

This project creates a chatbot that can have conversations with users. The bot learns from training data and gets better over time. It works in two ways:
1. **Web Interface**: Chat through a web browser
2. **Terminal Interface**: Chat through command line

The chatbot uses machine learning to understand what users say and give good responses.

## ✨ Features

- Web-based chat interface
- Terminal/command line chat
- Machine learning responses
- Pre-trained with English conversations
- Saves conversation history
- Clean and simple design
- Easy to use interface

## 🛠 Technology Stack

- **Backend**: Python, Django
- **AI Library**: ChatterBot
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Training Data**: ChatterBot Corpus

## Getting Started

### What You Need

- Python 3.9 or higher
- pip (Python package manager)
- Basic knowledge of using terminal

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-chatterbot-project.git
   cd django-chatterbot-project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**
   ```bash
   python manage.py migrate
   ```

4. **Run the web version**
   ```bash
   python manage.py runserver
   ```
   Open http://127.0.0.1:8000/ in your browser

5. **Run the terminal version**
   ```bash
   python terminal_chatbot.py
   ```

## 📦 Installation

### Step 1: Install Required Software

```bash
# Install Django
pip install django

# Install ChatterBot
pip install chatterbot==1.2.7

# Install ChatterBot training data
pip install chatterbot-corpus
```

### Step 2: Set Up Project

```bash
# Create project folder
mkdir chatbot_project
cd chatbot_project

# Clone or create the project files
# (Copy all files from this repository)

# Set up database
python manage.py makemigrations
python manage.py migrate
```

## Usage

### Web Interface

1. Start the Django server:
   ```bash
   python manage.py runserver
   ```

2. Open your web browser and go to: `http://127.0.0.1:8000/`

3. Type messages in the input box and press Enter or click Send

4. The bot will respond to your messages

### Terminal Interface

1. Run the terminal chatbot:
   ```bash
   python terminal_chatbot.py
   ```

2. Type your messages and press Enter

3. Type 'quit', 'exit', or 'bye' to stop chatting

### Example Conversation

```
You: Good morning! How are you doing?
Bot: I am doing very well, thank you for asking.

You: You're welcome.
Bot: Do you like hats?

You: Yes, I do like hats.
Bot: That's great! What kind of hats do you prefer?
```

## 📁 Project Structure

```
django-chatterbot-project/
├── README.md                    # Main project documentation
├── requirements.txt             # Python dependencies
├── manage.py                   # Django management script
├── terminal_chatbot.py         # Terminal chat interface
├── .gitignore                  # Git ignore file
├── docs/                       # Documentation folder
│   ├── INSTALLATION.md         # Detailed installation guide
│   ├── USAGE.md               # How to use the project
│   └── TROUBLESHOOTING.md     # Common problems and solutions
├── myproject/                  # Django project settings
│   ├── settings.py            # Django configuration
│   ├── urls.py                # Main URL routing
│   └── wsgi.py                # Web server interface
├── chatbot/                    # Main chatbot application
│   ├── views.py               # Web request handlers
│   ├── urls.py                # App URL routing
│   ├── bot.py                 # Chatbot logic
│   ├── templates/             # HTML templates
│   │   └── chatbot/
│   │       └── chat.html      # Main chat interface
│   └── static/                # CSS and JavaScript files
│       └── chatbot/
│           ├── css/style.css  # Styling
│           └── js/chat.js     # JavaScript logic
├── screenshots/                # Project screenshots
│   ├── web_interface.png      # Web chat screenshot
│   └── terminal_interface.png # Terminal chat screenshot
└── tests/                      # Test files
    └── test_chatbot.py        # Chatbot tests
```

## Screenshots

### Web Interface
Place your web interface screenshot here: `screenshots/web_interface.png`

### Terminal Interface
Place your terminal interface screenshot here: `screenshots/terminal_interface.png`

## 📚 References

1. ChatterBot Documentation. (2025). *About ChatterBot*. Retrieved from https://docs.chatterbot.us/
2. StudyGyaan. (2024). *Building Python Django Chatbot with Chatterbot*. Retrieved from https://studygyaan.com/django/building-python-django-chatbot-with-chatterbot
3. Real Python. (2023). *ChatterBot: Build a Chatbot With Python*. Retrieved from https://realpython.com/build-a-chatbot-python-chatterbot/