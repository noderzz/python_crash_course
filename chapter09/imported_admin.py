#Start with your work from Exercise 9-8 (page 173). Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.
from user_classes import User, Admin, Privileges

new_boss = Admin("boss123","pass123")
new_boss.privileges.show_privileges()