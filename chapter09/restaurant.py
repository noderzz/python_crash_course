'''
Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.

Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
'''
class Restaurant:
    ''' '''
    def __init__(self, name, cousine_type):
        '''The initial function that is run upon creation of an object from this class.'''
        self.name = name
        self.cousine_type = cousine_type
    
    def describe_restaurant(self):
        '''Describes cousine type of restaurant.'''
        print(f"The restaurant {self.name.title()} is a {self.cousine_type} restauruant.")

    def open_restaurant(self):
        '''Prints message that restaurant is open.'''
        print(f"{self.name.title()} is now open!")

place = Restaurant("yamatos", "sushi")
place.describe_restaurant()
place.open_restaurant()