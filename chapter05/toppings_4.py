requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping.lower() == "green peppers":
            print(f"Sorry, we are out of {requested_topping.title()}.")
        else:
            print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")