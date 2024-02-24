import random

# Define intents and responses
INTENTS = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "hello": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "greetings": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "goodbye": ["Goodbye!", "See you later!", "Have a great day!"],
    "faq": ["I'm sorry, I don't have that information right now."],
    "thanks": ["You're welcome!", "No problem!", "Happy to help!"]
}

def get_response(intent):
    if intent.lower() in INTENTS:
        responses = INTENTS[intent]
        return random.choice(responses)
    else:
        return "I'm sorry, I don't have that information right now."

def chat():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ").lower()
        response = get_response(user_input)
        print("Bot:", response)
        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break

# Start chatting
chat()