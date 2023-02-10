#The remember_me.py example only stores one piece of information, the username. Expand this example by asking for two more pieces of information about the user, then store all the information you collect in a dictionary. Write this dictionary to a file using json.dumps(), and read it back in using json.loads(). Print a summary showing exactly what your program remembers about the user.
from pathlib import Path
import json

def get_stored_info(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        information = json.loads(contents)
        return information
    else:
        return None
    
def get_new_info(path):
    """Prompt for a new username."""
    wanted_info = ["first name", "last name", "username", "password"]
    information = {}
    for item in wanted_info:
        response = input(f"Please enter your {item}: ")
        information[item] = response
    contents = json.dumps(information)
    path.write_text(contents)
    print("\nThank you for your information, we'll be sure to save it for next time.")
    return contents

def greet_user():
    """Greet the user by name."""
    path = Path('chapter10/username2.json')
    information = get_stored_info(path)
    if information:
        print(f"Welcome back!  Here is all the info we've saved on you!")
        for key,value in information.items():
            if key == "first name" or key == "last name":
                print(f"{key.title()}: {value.title()}")
            else:
                print(f"{key.title()}: {value}")
    else:
        get_new_info(path)

greet_user()