"""
Chatbot logic using ChatterBot library.

This module contains the main chatbot functionality including:
- Creating and configuring the chatbot
- Training the chatbot with data
- Getting responses from the chatbot
"""

import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from django.conf import settings

# Get the base directory of the Django project
BASE_DIR = getattr(settings, 'BASE_DIR', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def create_chatbot():
    """
    Create and configure the chatbot instance.

    Returns:
        ChatBot: Configured chatbot instance
    """
    bot = ChatBot(
        'DjangoChatBot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///chatbot_database.sqlite3',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I am sorry, but I do not understand. I am still learning.',
                'maximum_similarity_threshold': 0.90
            }
        ]
    )
    return bot

def train_chatbot(bot):
    """
    Train the chatbot with English corpus data and custom responses.

    Args:
        bot (ChatBot): The chatbot instance to train
    """
    # Train with English corpus
    trainer = ChatterBotCorpusTrainer(bot)
    trainer.train('chatterbot.corpus.english')

    # Train with custom conversation data
    list_trainer = ListTrainer(bot)

    # Custom training data for better responses
    custom_conversations = [
        "Hello",
        "Hi there! How can I help you today?",
        "How are you?",
        "I'm doing well, thank you for asking!",
        "What is your name?",
        "I'm a chatbot created with Django and ChatterBot. You can call me Django Bot!",
        "What can you do?",
        "I can chat with you and answer questions. I learn from our conversations!",
        "Thank you",
        "You're welcome! I'm here to help.",
        "Goodbye",
        "Goodbye! Have a great day!",
        "What is Django?",
        "Django is a high-level Python web framework that encourages rapid development and clean design.",
        "What is ChatterBot?",
        "ChatterBot is a Python library that makes it easy to generate automated responses to user inputs.",
        "Tell me a joke",
        "Why don't scientists trust atoms? Because they make up everything!",
    ]

    list_trainer.train(custom_conversations)

# Create a global chatbot instance
chatbot = create_chatbot()

# Train the chatbot when the module is imported
train_chatbot(chatbot)

def get_bot_response(user_input):
    """
    Get a response from the chatbot for the given user input.

    Args:
        user_input (str): The user's message

    Returns:
        str: The chatbot's response
    """
    try:
        # Get response from the chatbot
        response = chatbot.get_response(user_input)
        return str(response)
    except Exception as e:
        # Return a default response if there's an error
        return f"Sorry, I had trouble understanding that. Please try again."

def reset_chatbot():
    """
    Reset the chatbot by clearing its database.
    Use this function carefully as it will delete all learned conversations.
    """
    global chatbot
    try:
        # Clear the chatbot's storage
        chatbot.storage.drop()
        # Recreate and retrain the chatbot
        chatbot = create_chatbot()
        train_chatbot(chatbot)
        return True
    except Exception as e:
        return False