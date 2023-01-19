#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
invites = ['Ryan Reynolds', 'Chris Hemsworth', 'Chris Pratt', 'Henry Cavill', 'Karen Gillan', 'Emma Watson']

print(f"There are originally {len(invites)} guests on the list.\n")

print("The table is actually much smaller than we thought, we unfortunately can only invite 2 guests.")

name = invites.pop()
print(f"Dear {name}, I'm sorry but you didn't make the list.")
print(invites)

name = invites.pop()
print(f"Dear {name}, I'm sorry but you didn't make the list.")
print(invites)

name = invites.pop()
print(f"Dear {name}, I'm sorry but you didn't make the list.")
print(invites)

name = invites.pop()
print(f"Dear {name}, I'm sorry but you didn't make the list.\n")
print(invites)

name = invites.pop()
print(f"Dear {name}, congratulations you made the list!")
print(invites)

name = invites.pop()
print(f"Dear {name}, congratulations you made the list!")
print(invites)

