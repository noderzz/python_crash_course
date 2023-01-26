#Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”
car_type = input("Please enter what type of car you'd like: ")

if car_type[0].lower() in ["a","e","i","o"]:
    print(f"Let me see if we can find you an {car_type.title()}.")
else:
    print(f"Let me see if we can find you a {car_type.title()}.")