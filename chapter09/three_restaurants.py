'''
Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.
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
place2 = Restaurant("five guys", "burger")
place3 = Restaurant("red iguana", "Mexican")
place.describe_restaurant()
place2.describe_restaurant()
place3.describe_restaurant()
