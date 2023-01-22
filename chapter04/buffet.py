"""
 A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.

Use a for loop to print each food the restaurant offers.
Try to modify one of the items, and make sure that Python rejects the change.
The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
"""
basic_foods = ("fries", "steak","fried chicken", "shrimp","mashed potatoes")
#basic_foods[2] = "sushi" #This is the line that gives an error due to attempting to change the contents of the tuple.

print("The original items were:")
for food in basic_foods:
    print(food)

print("\nThe new items are:")
basic_foods = ("curly fries", "steak","fried chicken", "sushi","mashed potatoes")
for food in basic_foods:
    print(food)
