#Write a program that prompts for the user’s favorite number. Use json.dumps() to store this number in a file. Write a separate program that reads in this value and prints the message “I know your favorite number! It’s _____.”
from pathlib import Path
import json

path = Path("chapter10/favorite_number.json")
favorite_number = path.read_text()
json_number = json.loads(favorite_number)
print(f"Hey, I know your favorite number!\nIt's {json_number}!")