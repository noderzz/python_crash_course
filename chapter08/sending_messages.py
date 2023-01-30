#Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.
text_messages = [
    'Hey Tom, can you come into work early?',
    'New phone, who dis?',
    'Have you seen that meme yet? Ill send it to you!'
]
sent_messages = []

def send_messages(text_messages):
    while text_messages:
        message = text_messages.pop()
        print(message)
        sent_messages.append(message)

send_messages(text_messages)
print("\n")
print(sent_messages)
print(text_messages)