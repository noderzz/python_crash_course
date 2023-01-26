'''
Start with the program you wrote for Exercise 6-1 (page 99). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.
'''
person_01 = {'first_name':'joe', 'last_name':'johnson', 'age':35, 'city':'las vegas'}
person_02 = {'first_name':'jane', 'last_name':'austen', 'age':30, 'city':'new york'}
person_03 = {'first_name':'alex', 'last_name':'thompson', 'age':25, 'city':'los angeles'}

people = [person_01,person_02,person_03]

for person in people:
    print(f"Name: {person['first_name'].title()} {person['last_name'].title()}")
    print(f"\tAge: {person['age']}")
    print(f"\tLocation: {person['city'].title()}")