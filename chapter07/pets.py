pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

print("\nNow removing every instance of 'cat' starting from the beginning of the list:")
print(pets)
while 'cat' in pets:
    pets.remove('cat')
    print(pets)

print("\nThe list now looks like this:")
print(pets)