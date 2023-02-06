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
