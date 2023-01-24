#Generate list square numbers from 1-10
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

#More concise
squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)