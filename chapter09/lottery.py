#Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.
from random import randint
base_tuple = (1,2,3,4,5,6,7,8,9,0,"a","b","c","d","e")
winning = []

for i in range(0,4):
    winning.append(base_tuple[randint(0,14)])

print("Any ticket matching these 3 numbers or letters wins a prize!:")
print(f"{winning}")