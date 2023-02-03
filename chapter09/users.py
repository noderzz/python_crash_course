'''
Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user.

Create several instances representing different users, and call both methods for each user.
'''

class User:
    ''' '''
    def __init__(self, first_name, last_name, username='NOT SPECIFIED', age="NOT SPECIFIED", location="NOT SPECIFIED"):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.location = location

    def describe_user(self):
        '''Prints a summary of the users's information'''
        print(f"USERNAME: {self.username}\n\tFirst Name: {self.first_name.title()}\n\tLast Name: {self.last_name.title()}\n\tAge: {self.age}\n\tLocation: {self.location}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!")

guy = User("mike","johnson")
guy.describe_user()
guy.greet_user()