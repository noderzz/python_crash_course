#Write a while loop that prompts users for their name. Collect all the names that are entered, and then write these names to a file called guest_book.txt. Make sure each entry appears on a new line in the file.
from pathlib import Path

path = Path("chapter10/guest_book.txt")
guest = ''
guest_book = []
continue_writing = True

while continue_writing:
    print("Please enter 'q' at any time to quit")
    guest = input("Guests name: ")
    if guest.lower() == "q":
        continue_writing = False
    else:
        guest_book.append(guest)

guest = ''
for name in guest_book:
    guest += f"{name.title()}\n"

print("Now writing names to 'guest_book.txt'")
path.write_text(guest)