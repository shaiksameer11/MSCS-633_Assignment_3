"""
Django app configuration for the chatbot application.

This file defines the configuration for the chatbot app.
"""

from django.apps import AppConfig


class ChatbotConfig(AppConfig):
    """
    Configuration class for the chatbot application.

    This class defines the basic configuration for the chatbot app,
    including the default auto field type and the app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbot'
    verbose_name = 'Chatbot Application'