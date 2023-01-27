pizza_toppings = "Please enter all the pizza toppings you want!:"
pizza_toppings += "(Input 'quit' at anytime to end the program.)"

toppings = []

while True:
    topping = input(pizza_toppings)
    if topping == 'quit':
        print("Your total toppings are:")
        for item in toppings:
            print(item)
        break
    else:
        toppings.append(topping.title())
        print(f"{topping.title()} has now been added to your pizza!")