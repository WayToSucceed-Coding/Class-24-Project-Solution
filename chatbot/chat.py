# main.py

from chatbot.responses import get_response


def start_bot():
    print("Chatbot: Hi! Ask me something or type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        print(f"Chatbot: {responses.get_response(user_input)}")
