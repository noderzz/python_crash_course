available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Now adding {topping.title()} to your pizza.")
    else:
        print(f"Sorry, {topping.title()} is not an available topping.")