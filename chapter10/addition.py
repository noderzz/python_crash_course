#One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers. Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.
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