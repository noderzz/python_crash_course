#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.
pet_01 = {'name':'scruffy','kind':'dog','owner':'betty'}
pet_02 = {'name':'snowball','kind':'cat','owner':'rachel'}
pet_03 = {'name':'kyle','kind':'lizard','owner':'stephen'}

pets = [pet_01,pet_02,pet_03]

for pet in pets:
    print(f"Pet Name: {pet['name'].title()}")
    print(f"\tSpecies: {pet['kind'].title()}")
    print(f"\tOwner: {pet['owner'].title()}")