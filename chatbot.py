# chatbot.py

import random

# Simple pattern-response logic
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!", "Hi! How can I help you?"],
    "how are you": ["I'm good, thanks!", "Doing great, how about you?", "All systems go!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "your name": ["I'm ChatBot!", "You can call me Bot.", "I'm your friendly assistant."],
    "help": ["Ask me anything like: hello, how are you, your name, bye."]
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Sorry, I didn't understand that. Try 'help'."

def main():
    print("🤖 ChatBot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("🤖 ChatBot:", random.choice(responses["bye"]))
            break
        response = get_response(user_input)
        print("🤖 ChatBot:", response)

if __name__ == "__main__":
    main()
5