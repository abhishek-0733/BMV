def process_command(command):
    command = command.lower().strip()

    if command in ["hello", "hi", "hey"]:
        return "Hello! How can I help you?"

    elif command in ["what is your name", "your name"]:
        return "My name is BMV. I am your personal AI assistant."

    elif command in ["how are you", "how are you doing"]:
        return "I'm doing great! Ready to help you."

    elif command in ["who created you", "who made you"]:
        return "I was created as a personal AI assistant project."

    elif command in ["exit", "quit", "goodbye"]:
        return "Goodbye!"

    else:
        return "I don't understand that command yet."