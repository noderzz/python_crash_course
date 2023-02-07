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