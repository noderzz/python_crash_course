#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
invites = ["Ryan Reynolds", "Hugh Jackman", "Chris Pratt"]
place = invites.index("Hugh Jackman")
invites.insert(place,"Chris Hemsworth")
invites.remove('Hugh Jackman')

print("Since we have a bigger table we'll be inviting more guests!")

invites.append("Henry Cavill")
invites.append("Karen Gillan")
invites.append("Emma Watson")
print(invites)

name = invites.pop(0)
print(f"Dear {name}, you are invited to dinner.")
print(invites)

name = invites.pop(0)
print(f"Dear {name}, you are invited to dinner.")
print(invites)

name = invites.pop(0)
print(f"Dear {name}, you are invited to dinner.")
print(invites)

name = invites.pop(0)
print(f"Dear {name}, you are invited to dinner.")
print(invites)

name = invites.pop(0)
print(f"Dear {name}, you are invited to dinner.")
print(invites)

name = invites.pop(0)
print(f"Dear {name}, you are invited to dinner.")
print(invites)
