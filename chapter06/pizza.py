pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}
print(f"You ordered a {pizza['crust']}-crust pizza" 
    "with the following toppings:")

#Create a for loop based on the value (which is a list) for the key 'toppings'
for topping in pizza['toppings']:
    print(f"\t{topping}")