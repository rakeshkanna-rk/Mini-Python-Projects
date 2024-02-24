# Basic Chatbot

This is a simple chatbot implemented in Python. The chatbot is capable of responding to predefined intents and can engage in basic conversation with the user.

## Features

- Responds to greetings like "hi", "hello", and "greetings".
- Provides predefined responses for common interactions such as saying "thanks" or "goodbye".
- Handles some frequently asked questions (FAQs) with predefined responses.
- Allows users to interact with the chatbot through the command line interface.
- Your able to give custom commands and custom functions in get_response()

## Getting Started

To run the chatbot, you need to have Python installed on your system. Follow these steps to get started:

1. Clone this repository to your local machine.
2. Navigate to the directory where you cloned the repository.
3. Run the `ChatBot.py` script using Python: `python ChatBot.py`.
4. Start chatting with the bot in the command line interface.

## Usage

Once the chatbot is running, you can interact with it by typing messages in the command line interface. The chatbot will respond based on predefined intents and responses. Type "exit" to end the conversation and close the chatbot.

## How This Works

- The simple chatbot operates based on predefined intents and corresponding responses.
- When a user inputs a message, it is checked against a dictionary of intents, which represent various types of user interactions such as greetings, hi, hello, FAQs, and more.
- If the input matches an intent, the bot randomly selects a response associated with that intent.
- However, if the input does not match any intent, the bot provides a default response indicating that it doesn't have the requested information.
- This process enables the chatbot to engage in basic conversation with users via a command-line interface.
- The chatbot continuously prompts the user for input, processes the message, generates a response, and outputs it, creating a conversational loop.
- This straightforward approach allows users to interact with the bot seamlessly, making it an accessible tool for demonstrating natural language processing principles and conversational agent concepts using Python.

## Advance Version 
Advance version of the chatbot is available at [Simple-Chat-Bot](https://github.com/rakeshkanna-rk/Simple-Chat-Bot)