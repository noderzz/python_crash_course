def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#Order doesn't matter anymore because you're defining the variables
describe_pet(pet_name='harry',animal_type='hamster')