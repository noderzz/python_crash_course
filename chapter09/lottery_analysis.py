#You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.
from random import randint
base_tuple = (1,2,3,4,5,6,7,8,9,0,"a","b","c","d","e")
winning = []
my_ticket = []
counter = 0

for i in range(0,4):
    winning.append(base_tuple[randint(0,14)])

while my_ticket != winning:
    my_ticket = []
    counter += 1
    for i in range(0,4):
        my_ticket.append(base_tuple[randint(0,14)])

print("Hey, you won!")
print(f'Your ticket was "{my_ticket}"')
print(f'The winning ticket was "{winning}"')
print(f'To win it took you "{counter} number of tries!"')