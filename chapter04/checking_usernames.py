"""
Do the following to create a program that simulates how websites ensure that everyone has a unique username.

Make a list of five or more usernames called current_users.
Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
"""
current_users = ["admin","joe24","jill32","steve18","karen42"]
new_users = ["max123","steve18","kilee82","tiffany21","joe24"]
for i in new_users:
    if i.lower() in current_users:
        print(f"Sorry, the username {i} is taken.  Please choose a new name.")
    else:
        print(f"The username {i} looks to be available!")