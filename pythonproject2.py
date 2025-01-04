import webbrowser
import datetime
import random

# Function to handle commands
def handle_command(command):
    if "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google..."
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}."
    elif "joke" in command:
        jokes = [
            "Why don’t skeletons fight each other? They don’t have the guts!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don’t programmers like nature? It has too many bugs."
        ]
        return random.choice(jokes)
    elif "compliment me" in command:
        compliments = [
            "You have a great sense of humor!",
            "You're really good at what you do.",
            "You have an amazing smile!"
        ]
        return random.choice(compliments)
    elif "exit" in command or "quit" in command:
        return "Goodbye!"
    else:
        return "I'm not sure how to help with that."

# Main loop
def main():
    print("Hello! I am your assistant. Type 'exit' to quit.")
    while True:
        command = input("You: ").lower()
        response = handle_command(command)
        print(f"Bot: {response}")
        if response == "Goodbye!":
            break

# Run the assistant
if __name__ == "__main__":
    main()
