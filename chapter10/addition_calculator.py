#Wrap your code from Exercise 10-5 in a while loop so the user can continue entering numbers, even if they make a mistake and enter text instead of a number.
print("Please give me two numbers and I'll add them for you.")
print("Enter 'q' at any time to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number.lower() == 'q':
        break
    second_number = input("Second number: ")
    if second_number.lower() == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Please only provide numbers.")
    else:
        print(f"\nYour answer is {answer}")