"""
Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:

Use a conditional test in the while statement to stop the loop.
Use an active variable to control how long the loop runs.
Use a break statement to exit the loop when the user enters a 'quit' value.
"""
prompt = "Welcome to the movies!  Please enter your age: "
prompt = "(Please enter 'quit' at anytime to exit.)"

active = True

while active:
    age = input(prompt)
    
    if age == 'quit':
        print("Thank you for using our program!")
        active = False
    elif int(age) < 3:
        print(f"Admission is free for someone who is {age} years old.")
    elif int(age) <= 12:
        print(f"Admission is $10 for someone who is {age} years old.")
    elif int(age) > 12:
        print(f"Admission is $15 for someone who is {age} years old.")