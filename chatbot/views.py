"""
Django views for the chatbot application.

This module contains view functions that handle HTTP requests
and return HTTP responses for the chatbot web interface.
"""

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
import json
from .bot import get_bot_response


def home(request):
    """
    Display the main chat interface.

    This view renders the main chat page where users can
    interact with the chatbot through a web interface.

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: Rendered chat template
    """
    return render(request, 'chatbot/chat.html')


@csrf_exempt
def get_response(request):
    """
    Get chatbot response for user message.

    This view handles AJAX requests from the frontend to get
    chatbot responses. It accepts both GET and POST requests.

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        JsonResponse: JSON response containing bot's reply
    """
    if request.method == 'GET':
        # Handle GET request (message in URL parameters)
        user_message = request.GET.get('message', '').strip()
    elif request.method == 'POST':
        # Handle POST request (message in request body)
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').strip()
        except json.JSONDecodeError:
            user_message = request.POST.get('message', '').strip()
    else:
        return JsonResponse({
            'error': 'Method not allowed'
        }, status=405)

    # Check if message is provided
    if not user_message:
        return JsonResponse({
            'error': 'No message provided',
            'user_message': '',
            'bot_response': 'Please type a message!'
        })

    # Get response from chatbot
    try:
        bot_response = get_bot_response(user_message)
        return JsonResponse({
            'user_message': user_message,
            'bot_response': bot_response,
            'success': True
        })
    except Exception as e:
        return JsonResponse({
            'error': 'Failed to get bot response',
            'user_message': user_message,
            'bot_response': 'Sorry, I encountered an error. Please try again.',
            'success': False
        })


class ChatView(TemplateView):
    """
    Class-based view for the chat interface.

    This is an alternative to the function-based home view.
    You can use either approach - this one is more suitable
    for complex views that need additional functionality.
    """
    template_name = 'chatbot/chat.html'

    def get_context_data(self, **kwargs):
        """
        Add extra context data to the template.

        Returns:
            dict: Context data for the template
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Chat with Django Bot'
        context['welcome_message'] = 'Hello! I am a Django chatbot. How can I help you today?'
        return context


def about(request):
    """
    Display information about the chatbot.

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: Rendered about template
    """
    context = {
        'page_title': 'About Django ChatBot',
        'description': 'This chatbot is built using Django and ChatterBot library.',
        'features': [
            'Web-based chat interface',
            'Machine learning responses',
            'Learns from conversations',
            'Easy to extend and customize'
        ]
    }
    return render(request, 'chatbot/about.html', context)