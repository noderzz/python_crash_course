#Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.
places_dictionary = {}
while True:
    name = input("What is your name?\n")
    place = input("If you could visit one place in the world, where would you go?\n")

    places_dictionary[name] = place

    response = input("Would you like to poll someone else? (yes/no)")
    if response.lower() in ['no','n','nope']:
        break

print("\n-----Results of the Poll-----")
for name,place in places_dictionary.items():
    print(f"{name.title()} would like to visit {place.title()}.")
