import re
import random
from datetime import datetime

def chatbot():
    print("Assistant: Hello!")
    print("Assistant: May i know your name?\n")

    name = input("Enter your name: ")

    print(f"\nAssistant: Hello, {name}.How are you doing?")

    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "Why was the computer cold? It left its Windows open.",
        "Debugging is like being a detective in a crime movie where you are also the criminal."
    ]

    while True:
        try:
            user_input = input(f"{name}: ").strip()

            if not user_input:
                continue

            text = user_input.lower()

            if re.search(r'\b(bye|exit|quit|goodbye)\b', text):
                print(f"Assistant: Goodbye, {name}!")
                break

            elif re.search(r'\b(hi|hello|hey)\b', text):
                print(f"Assistant: Hello, {name}. How can I help you?")

            elif re.search(r'\b(how are you)\b', text):
                print("Assistant: I am doing well. Thank you for asking.")

            elif re.search(r'\b(who are you|your name)\b', text):
                print("Assistant: I am a simple chatbot created in Python.")

            elif re.search(r'\b(help)\b', text):
                print("""
Assistant Commands:
- hello
- time
- date
- joke
- help
- bye
- calc 5+3
""")

            elif re.search(r'\b(time)\b', text):
                print("Assistant:", datetime.now().strftime("%H:%M:%S"))

            elif re.search(r'\b(date)\b', text):
                print("Assistant:", datetime.now().strftime("%d-%m-%Y"))

            elif re.search(r'\b(joke)\b', text):
                print("Assistant:", random.choice(jokes))

            elif text.startswith("calc"):
                try:
                    expression = user_input[5:]
                    result = eval(expression)
                    print("Assistant: Result =", result)
                except:
                    print("Assistant: Invalid expression.")

            elif '?' in user_input:
                print("Assistant: That is an interesting question.")

            else:
                print("Assistant: I understand.")

        except KeyboardInterrupt:
            print("\nAssistant: Program terminated.")
            break

        except Exception:
            print("Assistant: An error occurred.")

if __name__ == "__main__":
    chatbot()
  
