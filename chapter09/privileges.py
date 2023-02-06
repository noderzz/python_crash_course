#Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.
class User:
    '''Gathers information about a user.'''
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login_attempts = 0
        self.permissions = False

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

class Admin(User):
    """A class to represent an admin user along with all their associated permissions."""
    def __init__(self, username, password):
        super().__init__(username, password)
        self.permissions = True
        self.privileges = Privileges(["Can Add Posts","Can Delete Posts","Can Edit Posts","Can Add Users","Can Delete Users","Can Ban Users"])

class Privileges():
    """Define"""
    def __init__(self, privileges):
        self.permissions = True
        self.privileges = privileges
    
    def show_privileges(self):
        """List permissions of the Admin user."""
        print("=====Permissions Granted=====")
        if self.permissions:
            for privilege in self.privileges:
                print(privilege)
        else:
            print("You can't do squat.")

new_instance = Admin("boop123", "pass123")
new_instance.privileges.show_privileges()
