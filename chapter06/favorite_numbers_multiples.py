#Modify your program from Exercise 6-2 (page 99) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.
favorite_numbers = {
    'jon':[27.23,342,52,65],
    'jane':[237,234,24,3,1],
    'sam':[2323,1234,2,4,312],
    'taylor':[2711,3334,532,5432,21],
    'alex':[17,34,543,1222,1342],
}

for name,numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")