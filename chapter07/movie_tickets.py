#A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
prompt = "Welcome to the movies!  Please enter your age: "
prompt = "(Please enter 'quit' at anytime to exit.)"
while True:
    age = input(prompt)
    
    if age == 'quit':
        print("Thank you for using our program!")
        break
    elif int(age) < 3:
        print(f"Admission is free for someone who is {age} years old.")
    elif int(age) <= 12:
        print(f"Admission is $10 for someone who is {age} years old.")
    elif int(age) > 12:
        print(f"Admission is $15 for someone who is {age} years old.")