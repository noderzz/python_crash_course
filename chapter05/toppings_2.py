requested_toppings = ["mushrooms","extra cheese"]
if "mushrooms" in requested_toppings:
    print("Adding Mushrooms")
if "pepperoni" in requested_toppings:
    print("Adding Pepperoni")
if "extra cheese" in requested_toppings:
    print("Adding Extra Cheese.")

#More efficient
for i in requested_toppings:
    print(f"Adding {i.title()}")
