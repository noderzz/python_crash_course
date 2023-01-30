#Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.
text_messages = [
    'Hey Tom, can you come into work early?',
    'New phone, who dis?',
    'Have you seen that meme yet? Ill send it to you!'
]
sent_messages = []

def send_messages(text_messages):
    while text_messages:
        message = text_messages.pop(0)
        print(message)
        sent_messages.append(message)

send_messages(text_messages[:])
print("\n")
print(sent_messages)
print(text_messages)