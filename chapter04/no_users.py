"""
Add an if test to hello_admin.py to make sure the list of users is not empty.

If the list is empty, print the message We need to find some users!
Remove all of the usernames from your list, and make sure the correct message is printed.
"""
#Normal list
usernames = ["admin","joe24","jill32","steve18","karen42"]
for name in usernames:
    if name == "admin":
        print("Hello admin, would you like a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again.")

print("\n")

#Empty list
usernames = []
if usernames:
    for name in usernames:
        if name == "admin":
            print("Hello admin, would you like a status report?")
        else:
            print(f"Hello {name}, thank you for logging in again.")
print("We need to find some users!")