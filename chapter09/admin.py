#An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.
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

    def list_permissions(self):
        """List permissions of the Admin user."""
        print("=====Permissions Granted=====")
        if self.permissions:
            print("Can Add Posts\nCan Delete Posts\nCan Add Users\nCan Delete Users\nCan Ban Users")
        else:
            print("You can't do squat.")

bob123 = Admin("bob123","pass123")
bob123.list_permissions()
