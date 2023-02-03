"""
Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0.

Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
"""
class User:
    '''Gathers information about a user.'''
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login_attempts = 0

    def login(self, username, password):
        if username != self.username:
            self.login_attempts += 1
            print("Incorrect username or password.")
        elif password != self.password:
            self.login_attempts += 1
            print("Incorrect username or password.")
        else:
            print("Login Successful!")
    
    def display_login_attempts(self):
        print(f"Total login attempts are: {self.login_attempts}.")

    def reset_login_attempts(self):
        self.login_attempts = 0

barb = User("barb23","password2")

print("\n======Now attempting to login======")
barb.login("wrong_username","wrong_password")
barb.login("wrong_username","wrong_password")
barb.login("wrong_username","wrong_password")
barb.login("wrong_username","wrong_password")
barb.login("wrong_username","wrong_password")
barb.login("barb23","password2")

barb.display_login_attempts()
print("\n======Now reseting login attempts======")
barb.reset_login_attempts()
barb.display_login_attempts()