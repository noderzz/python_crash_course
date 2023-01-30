def make_pizza(*toppings):
    print(f"\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping.title()}")

make_pizza('pepperoni')
make_pizza('pepperoni','mushrooms','green peppers','chicken')

    