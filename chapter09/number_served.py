"""
Start with your program from Exercise 9-1 (page 162). Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again.

Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business.
"""
class Restaurant:
    ''' '''
    def __init__(self, name, cousine_type):
        '''The initial function that is run upon creation of an object from this class.'''
        self.name = name
        self.cousine_type = cousine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        '''Describes cousine type of restaurant.'''
        print(f"The restaurant {self.name.title()} is a {self.cousine_type} restauruant.")

    def open_restaurant(self):
        '''Prints message that restaurant is open.'''
        print(f"{self.name.title()} is now open!")

    def set_number_served(self,customers):
        self.number_served = customers

    def increment_number_served(self, increment_value):
            self.number_served += increment_value

restaurant = Restaurant("tonys","pizza")
restaurant.describe_restaurant()
print("Part one of question.")
print(restaurant.number_served)
restaurant.number_served = 25
print(restaurant.number_served)
print("\n")

print("Part two of question.")
print(restaurant.number_served)
restaurant.set_number_served(42)
print(restaurant.number_served)
print("\n")

print("Part three of question.")
print(restaurant.number_served)
restaurant.increment_number_served(74)
print(restaurant.number_served)