"""
Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:

Add a new pizza to the original list.
Add a different pizza to the list friend_pizzas.
Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
"""

pizza_flavors = ["BBQ Chicken","Pepperoni","Garlic Parmesan"]
friends_pizzas = pizza_flavors[:]

pizza_flavors.append("Spinach Artichoke")
friends_pizzas.append("Cheese")

print("My favorite pizza flavors are:")
for i in pizza_flavors:
    print(i)

print("\n")

print("My friends favorite pizza flavors are:")
for i in friends_pizzas:
    print(i)