#Ask the user for a number, and then report whether the number is a multiple of 10 or not
number = input("Please give me a number: ")
number = int(number)

if number % 10 == 0:
    print("This number is a multiple of 10!")
else:
    print("This number is not a multiple of ten.")