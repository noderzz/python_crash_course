#Combine the two programs you wrote in Exercise 10-11 into one file. If the number is already stored, report the favorite number to the user. If not, prompt for the user’s favorite number and store it in a file. Run the program twice to see that it works.
from pathlib import Path
import json

path = Path("chapter10/favorite_number.json")
if path.exists():
    favorite_number = path.read_text()
    json_number = json.loads(favorite_number)
    print(f"Hey, I know your favorite number!\nIt's {json_number}!")
else:
    favorite_number = input("What is your favorite number? ")
    path = Path("chapter10/favorite_number.json")
    json_number = json.dumps(int(favorite_number))
    path.write_text(json_number)
    print("I'll remember that for next time!")