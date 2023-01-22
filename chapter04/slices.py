"""
Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:

Print the message The first three items in the list are:. Then use a slice to print the first three items from that programs list.
Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
Print the message The last three items in the list are:. Use a slice to print the last three items in the list.
"""

players = ['charles', 'martina', 'michael', 'florence', 'eli', 'brandon','jacob',]
print("First three players are:")
print([x.title() for x in players[:3]])
print("\n")
print("Middle three players are:")
print([x.title() for x in players[2:5]])
print("\n")
print("Last three players are:")
print([x.title() for x in players[-3:]])