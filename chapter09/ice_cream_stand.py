"""
 An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.
"""
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

class IceCreamStand(Restaurant):
    """Describing a type of Ice-cream restaurant."""
    def __init__(self, name, flavors):
        super().__init__(name, cousine_type="Ice Cream")
        self.flavors = flavors

    def give_flavors(self):
        """List the Ice-cream flavors available."""
        print(f"===Available flavors at {self.name.title()} are as follows:===")
        for flavor in self.flavors:
            print(f"{flavor.title()}")

baskin_robins = IceCreamStand("baskin robins", ["chocolate","vanilla","strawberry","rocky road","cookies and cream","mint chocolate chip"])
baskin_robins.give_flavors()

    