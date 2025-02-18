import random
chatbot_responses = {
    "hello": ["Hi there! 😊", "Hello! 👋", "Hey! How's it going? 😃"],
    "how are you": ["I'm just a bot, but I'm doing great! 🤖", "I'm fine, thank you! How about you? 😊", "Feeling awesome today! 😎"],
    "what's your name": ["I'm ChatBot! 🤖 Nice to meet you!", "You can call me CodeAlpha Bot! 😃"],
    "bye": ["Goodbye! 👋 Have a great day!", "See you later! 😊", "Bye! Take care! 😃"],
    "thank you": ["You're welcome! 😊", "No problem! 😃", "Happy to help! 🤖"],
    "tell me a joke": [
        "Why did the programmer go broke? Because he used up all his cache! 😂",
        "I told my computer a joke... but it didn’t laugh. Guess it didn’t have enough bytes! 🤖",
        "Why don’t programmers like nature? Too many bugs! 🐛😂"
    ],
    "what can you do": [
        "I can chat with you, tell jokes, and keep you entertained! 🤖",
        "I can respond to your messages and make your day better! 😃",
        "I can provide fun facts, jokes, and friendly conversation! 🚀"
    ],
    "tell me a fun fact": [
        "Did you know? The first computer bug was a real insect! 🐛",
        "Fun fact: The Python programming language is named after Monty Python, not the snake! 🐍😂",
        "Here’s a cool one: The first-ever website is still online! 🌐"
    ],
    "default": ["I'm not sure how to respond to that. 🤔", "Can you rephrase? 😕", "Hmm... I don't understand that yet. 🤖"]
}

def chatbot():
    """A fun chatbot that responds to user inputs with predefined responses and emojis."""
    print("Chatbot: Hello! 😊 Type 'bye' to exit.")

    while True:
        user_message = input("You: ").lower()

        if user_message == "bye":
            print("Chatbot:", random.choice(chatbot_responses["bye"]))
            break
        else:
            response = chatbot_responses.get(user_message, random.choice(chatbot_responses["default"]))
            print("Chatbot:", random.choice(response))

if __name__ == "__main__":
    chatbot()


