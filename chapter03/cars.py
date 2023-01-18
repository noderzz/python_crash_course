#Permanently sort list alphabetically
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#Permanently reverse sort alphabetically
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#Temporarily sort alphabetically
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"The original list is \n{cars}.")
print(f"The temporarily sorted list is \n{sorted(cars)}.")
print(f"The original list again is \n{cars}.")

#Temporarily sort reverse-alphabetically
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"The original list is \n{cars}.")
print(f"The temporarily sorted list is \n{sorted(cars, reverse=True)}.")
print(f"The original list again is \n{cars}.")
