''''
Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
'''
person = {
    'first_name':'joe',
    'last_name':'johnson',
    'age':35,
    'city':'las vegas',
}

print(f"Here is information on {person['first_name'].title()} {person['last_name'].title()}:")
print(f"\tThe city {person['first_name'].title()} {person['last_name'].title()} lives in is {person['city'].title()}.")
print(f"\tThe age of {person['first_name'].title()} {person['last_name'].title()} is {person['age']} years old.")

