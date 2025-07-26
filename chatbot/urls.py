"""
URL configuration for the chatbot application.

This file defines the URL patterns for the chatbot app,
mapping URLs to their corresponding view functions.
"""

from django.urls import path
from . import views

# App namespace for URL reversing
app_name = 'chatbot'

urlpatterns = [
    # Main chat interface
    # URL: http://127.0.0.1:8000/
    path('', views.home, name='home'),

    # Alternative class-based view for chat interface
    # URL: http://127.0.0.1:8000/chat/
    path('chat/', views.ChatView.as_view(), name='chat'),

    # AJAX endpoint for getting bot responses
    # URL: http://127.0.0.1:8000/get-response/
    path('get-response/', views.get_response, name='get_response'),

    # About page
    # URL: http://127.0.0.1:8000/about/
    path('about/', views.about, name='about'),
]