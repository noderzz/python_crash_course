"""
The final listing for remember_me.py assumes either that the user has already entered their username or that the program is running for the first time. We should modify it in case the current user is not the person who last used the program.

Before printing a welcome back message in greet_user(), ask the user if this is the correct username. If its not, call get_new_username() to get the correct username.
"""
from pathlib import Path
import json

def get_stored_info(path):
    """Get stored information if available."""
    if path.exists():
        information = json.loads(path.read_text())
        username = information["username"]
        answer = input(f"Is this user {username}? (y/n)")
        if answer.lower() in ["y","yes","yup"]:        
            contents = path.read_text()
            information = json.loads(contents)
            return information
    else:
        return None
    
def get_new_info(path):
    """Prompt for new information."""
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
    """Display all data we have on the user."""
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