# Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.
name = "  Hugh Jackman  "

#Printing name normally
print(name)

#Printing name without spaces
print(name.rstrip().lstrip())
print(name.strip())