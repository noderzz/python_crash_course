"""
Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user:

If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
"""
usernames = ["admin","joe24","jill32","steve18","karen42"]
for name in usernames:
    if name == "admin":
        print("Hello admin, would you like a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again.")