"""
Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

Write an if statement to test whether the aliens color is green. If it is, print a message that the player just earned 5 points.
Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
"""
#Version 1
alien_color = "Yellow"
if alien_color.lower() == "green":
    score = 5
elif alien_color.lower() == "yellow":
    score = 10
elif alien_color.lower() == "red":
    score = 15
print(f"You got {score} points!")

#Version 2
alien_color = "blue"
if alien_color.lower() == "green":
    scores = 5
elif alien_color.lower() == "yellow":
    scores = 10
elif alien_color.lower() == "red":
    scores = 15

