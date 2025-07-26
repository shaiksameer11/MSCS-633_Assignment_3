"""
Terminal Chatbot - A simple command line chatbot using ChatterBot

This script creates a chatbot that runs in the terminal/command line.
Users can type messages and get responses from the AI chatbot.

Usage:
    python terminal_chatbot.py

Commands:
    - Type any message to chat with the bot
    - Type 'quit', 'exit', or 'bye' to stop the program
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def create_chatbot():
    """
    Create and train the chatbot.

    Returns:
        ChatBot: Trained chatbot instance
    """
    print("Setting up the chatbot...")

    # Create chatbot instance
    bot = ChatBot(
        'TerminalBot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///terminal_bot.sqlite3'
    )

    # Train the chatbot with English language data
    trainer = ChatterBotCorpusTrainer(bot)
    trainer.train('chatterbot.corpus.english')

    print("Chatbot is ready!")
    return bot

def start_chat():
    """
    Start the terminal chat interface.

    This function handles the main chat loop where users can
    type messages and receive responses from the chatbot.
    """
    # Create and train the chatbot
    bot = create_chatbot()

    # Print welcome message
    print("\n" + "="*50)
    print("Welcome to Terminal Chatbot!")
    print("Type 'quit', 'exit', or 'bye' to stop chatting")
    print("="*50)

    # Main chat loop
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()

        # Check if user wants to quit
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Bot: Goodbye! Have a great day!")
            break

        # Skip empty inputs
        if not user_input:
            print("Bot: Please type something!")
            continue

        # Get bot response
        try:
            response = bot.get_response(user_input)
            print(f"Bot: {response}")
        except Exception as e:
            print(f"Bot: Sorry, I had trouble understanding that. Error: {e}")

def main():
    """
    Main function to run the terminal chatbot.
    """
    try:
        start_chat()
    except KeyboardInterrupt:
        print("\n\nBot: Goodbye! Thanks for chatting!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please make sure ChatterBot is properly installed.")

if __name__ == "__main__":
    main()