"""
Tests for the chatbot application.

This module contains unit tests for the chatbot functionality,
including views, models, and bot responses.
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
import json
from .models import ChatSession, ChatMessage
from .bot import get_bot_response


class ChatbotViewsTestCase(TestCase):
    """
    Test cases for chatbot views.
    """

    def setUp(self):
        """Set up test client and data."""
        self.client = Client()

    def test_home_view(self):
        """Test that home view renders correctly."""
        response = self.client.get(reverse('chatbot:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Chat with My Bot')

    def test_get_response_view_with_message(self):
        """Test get_response view with valid message."""
        response = self.client.get(
            reverse('chatbot:get_response'),
            {'message': 'Hello'}
        )
        self.assertEqual(response.status_code, 200)

        # Parse JSON response
        data = json.loads(response.content)
        self.assertIn('user_message', data)
        self.assertIn('bot_response', data)
        self.assertEqual(data['user_message'], 'Hello')
        self.assertTrue(len(data['bot_response']) > 0)

    def test_get_response_view_without_message(self):
        """Test get_response view without message."""
        response = self.client.get(reverse('chatbot:get_response'))
        self.assertEqual(response.status_code, 200)

        # Parse JSON response
        data = json.loads(response.content)
        self.assertIn('error', data)

    def test_get_response_post_method(self):
        """Test get_response view with POST method."""
        response = self.client.post(
            reverse('chatbot:get_response'),
            data=json.dumps({'message': 'Hi there'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)

        # Parse JSON response
        data = json.loads(response.content)
        self.assertIn('user_message', data)
        self.assertIn('bot_response', data)

    def test_about_view(self):
        """Test about view renders correctly."""
        response = self.client.get(reverse('chatbot:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'About Django ChatBot')


class ChatbotModelsTestCase(TestCase):
    """
    Test cases for chatbot models.
    """

    def test_chat_session_creation(self):
        """Test creating a ChatSession."""
        session = ChatSession.objects.create(session_id='test_session_001')
        self.assertEqual(session.session_id, 'test_session_001')
        self.assertIsNotNone(session.created_at)
        self.assertIsNotNone(session.updated_at)

    def test_chat_message_creation(self):
        """Test creating a ChatMessage."""
        session = ChatSession.objects.create(session_id='test_session_002')
        message = ChatMessage.objects.create(
            session=session,
            user_message='Hello',
            bot_response='Hi there!'
        )
        self.assertEqual(message.user_message, 'Hello')
        self.assertEqual(message.bot_response, 'Hi there!')
        self.assertEqual(message.session, session)
        self.assertIsNotNone(message.timestamp)

    def test_chat_session_str_method(self):
        """Test ChatSession string representation."""
        session = ChatSession.objects.create(session_id='test_session_003')
        self.assertEqual(str(session), 'Chat Session test_session_003')


class ChatbotLogicTestCase(TestCase):
    """
    Test cases for chatbot logic and responses.
    """

    def test_get_bot_response_basic(self):
        """Test basic bot response functionality."""
        response = get_bot_response('Hello')
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)

    def test_get_bot_response_empty_input(self):
        """Test bot response with empty input."""
        response = get_bot_response('')
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)

    def test_get_bot_response_common_greetings(self):
        """Test bot responses to common greetings."""
        greetings = ['Hello', 'Hi', 'Hey', 'Good morning']

        for greeting in greetings:
            response = get_bot_response(greeting)
            self.assertIsInstance(response, str)
            self.assertTrue(len(response) > 0)

    def test_get_bot_response_questions(self):
        """Test bot responses to common questions."""
        questions = [
            'How are you?',
            'What is your name?',
            'What can you do?'
        ]

        for question in questions:
            response = get_bot_response(question)
            self.assertIsInstance(response, str)
            self.assertTrue(len(response) > 0)


class ChatbotIntegrationTestCase(TestCase):
    """
    Integration tests for the complete chatbot functionality.
    """

    def test_full_conversation_flow(self):
        """Test a complete conversation flow through the web interface."""
        # Test home page loads
        response = self.client.get(reverse('chatbot:home'))
        self.assertEqual(response.status_code, 200)

        # Test first message
        response = self.client.get(
            reverse('chatbot:get_response'),
            {'message': 'Hello'}
        )
        self.assertEqual(response.status_code, 200)
        data1 = json.loads(response.content)

        # Test follow-up message
        response = self.client.get(
            reverse('chatbot:get_response'),
            {'message': 'How are you?'}
        )
        self.assertEqual(response.status_code, 200)
        data2 = json.loads(response.content)

        # Verify responses are different (basic check)
        self.assertNotEqual(data1['bot_response'], data2['bot_response'])

    def test_multiple_concurrent_sessions(self):
        """Test handling multiple chat sessions."""
        client1 = Client()
        client2 = Client()

        # Send messages from both clients
        response1 = client1.get(
            reverse('chatbot:get_response'),
            {'message': 'Hello from client 1'}
        )
        response2 = client2.get(
            reverse('chatbot:get_response'),
            {'message': 'Hello from client 2'}
        )

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)

        data1 = json.loads(response1.content)
        data2 = json.loads(response2.content)

        self.assertIn('bot_response', data1)
        self.assertIn('bot_response', data2)