print("================================")
print("       BMV AI ASSISTANT")
print("================================")
print("Type 'exit' to close BMV.\n")

while True:
    user_command = input("You: ")

    if user_command.lower() == "exit":
        print("BMV: Goodbye!")
        break

    elif user_command.lower() == "hello":
        print("BMV: Hello! How can I help you?")

    elif user_command.lower() == "what is your name":
        print("BMV: My name is BMV. I am your personal AI assistant.")

    else:
        print("BMV: I don't understand that command yet.")