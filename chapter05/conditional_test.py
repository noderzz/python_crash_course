"""
You don’t have to limit the number of tests you create to ten. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:
"""

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\n")

#Test for equality and inequality with strings.
string = "I don't like jogging."
print("Test 1")
if string == "I do like jogging.":
    print(True)
else:
    print(False)
    
print("\n")

#Tests using the lower() method.
string = "I don't like jogging."
print("Test 2")
if string.lower() == "i don't like jogging.":
    print(True)
else:
    print(False)

print("\n")

#Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to.
number = 10
print("Test 3")
if number >= 5 and number <= 15:
    print(True)
else:
    print(False)

print("\n")

#Tests using the and keyword and the or keyword.
number = 9
print("Test 4")
if number <= 5 or number >= 10:
    print(True)
else:
    print(False)

print("\n")

#Test whether an item is in a list.
some_list = [1,2,3,4,6,7,8,9,10]
print("Test 5")
if 5 in some_list:
    print(True)
else:
    print(False)

print("\n")

#Test whether an item is not in a list.
some_list = [1,2,3,4,6,7,8,9,10]
print("Test 5")
if 5 not in some_list:
    print(True)
else:
    print(False)