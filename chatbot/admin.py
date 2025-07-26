"""
Django admin configuration for the chatbot application.

This file registers models with the Django admin interface
so they can be managed through the web-based admin panel.
"""

from django.contrib import admin
from .models import ChatSession, ChatMessage


@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    """
    Admin configuration for ChatSession model.
    """
    list_display = ('session_id', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('session_id',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    """
    Admin configuration for ChatMessage model.
    """
    list_display = ('get_session_id', 'user_message_preview', 'bot_response_preview', 'timestamp')
    list_filter = ('timestamp', 'session')
    search_fields = ('user_message', 'bot_response')
    readonly_fields = ('timestamp',)
    ordering = ('-timestamp',)

    def get_session_id(self, obj):
        """Get session ID for display in admin list."""
        return obj.session.session_id if obj.session else 'No Session'
    get_session_id.short_description = 'Session ID'

    def user_message_preview(self, obj):
        """Show preview of user message in admin list."""
        return obj.user_message[:50] + '...' if len(obj.user_message) > 50 else obj.user_message
    user_message_preview.short_description = 'User Message'

    def bot_response_preview(self, obj):
        """Show preview of bot response in admin list."""
        return obj.bot_response[:50] + '...' if len(obj.bot_response) > 50 else obj.bot_response
    bot_response_preview.short_description = 'Bot Response'