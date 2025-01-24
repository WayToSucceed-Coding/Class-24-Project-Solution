# responses.py

# Predefined responses
response_dict = {
    "hello": "Hi there!",
    "how are you": "I'm doing well, thank you!",
    "bye": "Goodbye!",
    "default": "I'm not sure what you mean."
}

# Function to fetch response
def get_response(user_input):
    return response_dict.get(user_input.lower(), response_dict["default"])
