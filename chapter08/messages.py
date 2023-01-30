#Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.
text_messages = [
    'Hey Tom, can you come into work early?',
    'New phone, who dis?',
    'Have you seen that meme yet? Ill send it to you!'
]

def show_messages(text_messages):
    for text in text_messages:
        print(text)

show_messages(text_messages)