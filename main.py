from ai.brain import ask_bmv


print("================================")
print("       BMV AI ASSISTANT")
print("================================")
print("Type 'exit' to close BMV.\n")


while True:
    user_command = input("You: ")

    if user_command.lower().strip() in ["exit", "quit", "goodbye"]:
        print("BMV: Goodbye!")
        break

    try:
        response = ask_bmv(user_command)
        print(f"BMV: {response}\n")

    except Exception as error:
        print(f"BMV: Sorry, something went wrong.")
        print(f"Error: {error}\n")