"""
Django models for the chatbot application.

This file defines the database models for storing chat-related data.
Currently, we rely on ChatterBot's built-in storage system,
but you can add custom models here if needed.
"""

from django.db import models
from django.utils import timezone


class ChatSession(models.Model):
    """
    Model to track chat sessions (optional).

    This model can be used to track different chat sessions
    if you want to implement session management.
    """
    session_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Chat Session {self.session_id}"


class ChatMessage(models.Model):
    """
    Model to store individual chat messages (optional).

    This model can be used to store chat history
    if you want to implement custom message storage.
    """
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, null=True, blank=True)
    user_message = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"Message at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"