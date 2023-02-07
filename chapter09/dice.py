"""
Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times.

Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""
from random import randint

class Die:
    """Class to roll a dice."""
    def __init__(self, sides=6):
        """Helps to set the initial value of how many sides your dice has."""
        self.sides = sides

    def roll_dice(self):
        """Give you a random number based on the number of sides your dice has."""
        value = randint(1,self.sides)
        print(f"You rolled a {value}!")

#Six Sides
six_sides = Die()
print("===SIX Sided Die===")
for i in range(1,11):
    six_sides.roll_dice()
print("\n")

#Ten Sides
six_sides = Die(10)
print("===TEN Sided Die===")
for i in range(1,11):
    six_sides.roll_dice()
print("\n")

#Twenty Sides
six_sides = Die(20)
print("===TWENTY Sided Die===")
for i in range(1,11):
    six_sides.roll_dice()

