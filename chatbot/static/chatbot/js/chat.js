/**
 * Django ChatBot - JavaScript functionality
 *
 * This file contains all the JavaScript functions for the chat interface,
 * including message handling, UI interactions, and API communication.
 */

// Global variables
let messageCount = 0;
let isTyping = false;

/**
 * Initialize the chat interface when the page loads
 */
document.addEventListener('DOMContentLoaded', function() {
    initializeChat();
});

/**
 * Initialize chat functionality
 */
function initializeChat() {
    // Focus on input field
    const userInput = document.getElementById('user-input');
    if (userInput) {
        userInput.focus();

        // Add event listeners
        userInput.addEventListener('keypress', handleKeyPress);
        userInput.addEventListener('input', handleInputChange);
    }

    // Add click listener to send button
    const sendButton = document.getElementById('send-button');
    if (sendButton) {
        sendButton.addEventListener('click', sendMessage);
    }

    // Add timestamp to welcome message
    updateMessageTimestamps();

    // Set up auto-scroll
    setupAutoScroll();

    console.log('Chat initialized successfully');
}

/**
 * Handle keypress events in the input field
 */
function handleKeyPress(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
}

/**
 * Handle input changes (for character count, etc.)
 */
function handleInputChange(event) {
    const input = event.target;
    const maxLength = input.maxLength;
    const currentLength = input.value.length;

    // You can add character count display here if needed
    // Example: showCharacterCount(currentLength, maxLength);
}

/**
 * Send a message to the chatbot
 */
function sendMessage() {
    const userInput = document.getElementById('user-input');
    const message = userInput.value.trim();

    // Validate input
    if (!message) {
        userInput.focus();
        return;
    }

    if (isTyping) {
        console.log('Bot is typing, please wait...');
        return;
    }

    // Disable controls
    setControlsEnabled(false);

    // Show user message
    addMessage('User', message, 'user-message');

    // Clear input
    userInput.value = '';

    // Show typing indicator
    showTypingIndicator();

    // Send request to server
    sendMessageToServer(message)
        .then(response => {
            hideTypingIndicator();

            if (response.success && response.bot_response) {
                addMessage('Bot', response.bot_response, 'bot-message');
            } else {
                addMessage('Bot', response.bot_response || 'Sorry, I encountered an error. Please try again.', 'bot-message error');
            }
        })
        .catch(error => {
            console.error('Error sending message:', error);
            hideTypingIndicator();
            addMessage('Bot', 'Sorry, I had trouble connecting. Please check your internet and try again.', 'bot-message error');
        })
        .finally(() => {
            setControlsEnabled(true);
            userInput.focus();
        });
}

/**
 * Send message to server and return promise
 */
async function sendMessageToServer(message) {
    const url = `/get-response/?message=${encodeURIComponent(message)}`;

    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Network error:', error);
        throw error;
    }
}

/**
 * Add a message to the chat
 */
function addMessage(sender, message, cssClass) {
    const chatMessages = document.getElementById('chat-messages');
    if (!chatMessages) return;

    messageCount++;

    // Create message element
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${cssClass}`;
    messageDiv.setAttribute('data-message-id', messageCount);

    const currentTime = getCurrentTime();
    const escapedMessage = escapeHtml(message);

    messageDiv.innerHTML = `
        <div class="message-content">
            <strong>${sender}:</strong> ${escapedMessage}
        </div>
        <div class="message-time">${currentTime}</div>
    `;

    // Add to chat
    chatMessages.appendChild(messageDiv);

    // Animate message appearance
    animateMessageIn(messageDiv);

    // Scroll to bottom
    scrollToBottom();

    // Log message for debugging
    console.log(`${sender}: ${message}`);
}

/**
 * Animate message appearance
 */
function animateMessageIn(messageElement) {
    messageElement.style.opacity = '0';
    messageElement.style.transform = 'translateY(20px)';

    // Trigger animation
    requestAnimationFrame(() => {
        messageElement.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
        messageElement.style.opacity = '1';
        messageElement.style.transform = 'translateY(0)';
    });
}

/**
 * Show typing indicator
 */
function showTypingIndicator() {
    isTyping = true;
    const indicator = document.getElementById('typing-indicator');
    if (indicator) {
        indicator.style.display = 'block';
        scrollToBottom();
    }
}

/**
 * Hide typing indicator
 */
function hideTypingIndicator() {
    isTyping = false;
    const indicator = document.getElementById('typing-indicator');
    if (indicator) {
        indicator.style.display = 'none';
    }
}

/**
 * Enable or disable input controls
 */
function setControlsEnabled(enabled) {
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    if (userInput) {
        userInput.disabled = !enabled;
    }

    if (sendButton) {
        sendButton.disabled = !enabled;
    }
}

/**
 * Scroll chat to bottom
 */
function scrollToBottom() {
    const chatMessages = document.getElementById('chat-messages');
    if (chatMessages) {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
}

/**
 * Set up auto-scroll functionality
 */
function setupAutoScroll() {
    const chatMessages = document.getElementById('chat-messages');
    if (!chatMessages) return;

    // Auto-scroll when new content is added
    const observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
            if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
                scrollToBottom();
            }
        });
    });

    observer.observe(chatMessages, {
        childList: true,
        subtree: true
    });
}

/**
 * Get current time formatted for display
 */
function getCurrentTime() {
    const now = new Date();
    return now.toLocaleTimeString([], {
        hour: '2-digit',
        minute: '2-digit'
    });
}

/**
 * Update timestamps on existing messages
 */
function updateMessageTimestamps() {
    const timeElements = document.querySelectorAll('.message-time');
    const currentTime = getCurrentTime();

    timeElements.forEach(element => {
        if (!element.textContent) {
            element.textContent = currentTime;
        }
    });
}

/**
 * Escape HTML to prevent XSS
 */
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

/**
 * Clear chat history
 */
function clearChat() {
    const chatMessages = document.getElementById('chat-messages');
    if (!chatMessages) return;

    // Confirm with user
    if (confirm('Are you sure you want to clear the chat history?')) {
        chatMessages.innerHTML = `
            <div class="message bot-message">
                <div class="message-content">
                    <strong>Bot:</strong> Chat history cleared. How can I help you today?
                </div>
                <div class="message-time">${getCurrentTime()}</div>
            </div>
        `;
        messageCount = 0;
        console.log('Chat history cleared');
    }
}

/**
 * Handle window resize for responsive design
 */
function handleResize() {
    // Adjust chat height if needed
    const container = document.querySelector('.container');
    const header = document.querySelector('.chat-header');
    const inputContainer = document.querySelector('.chat-input-container');
    const chatContainer = document.querySelector('.chat-container');

    if (container && header && inputContainer && chatContainer) {
        const headerHeight = header.offsetHeight;
        const inputHeight = inputContainer.offsetHeight;
        const availableHeight = window.innerHeight - headerHeight - inputHeight - 40;

        chatContainer.style.height = Math.max(300, availableHeight) + 'px';
    }
}

/**
 * Initialize resize handling
 */
window.addEventListener('load', handleResize);
window.addEventListener('resize', handleResize);

/**
 * Handle connection errors
 */
function handleConnectionError() {
    addMessage('System', 'Connection lost. Please check your internet connection.', 'bot-message error');
}

/**
 * Retry sending message
 */
function retryLastMessage() {
    // Implementation for retrying last message
    console.log('Retry functionality not implemented yet');
}

/**
 * Export functions for external use
 */
window.ChatBot = {
    sendMessage,
    clearChat,
    addMessage,
    setControlsEnabled,
    scrollToBottom
};

// Debug mode
if (window.location.search.includes('debug=true')) {
    window.ChatBot.debug = true;
    console.log('ChatBot debug mode enabled');
}