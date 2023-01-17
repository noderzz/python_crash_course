#Set variable
example = "  two spaces to the left and right  "
print(example)

#Strip whitespace from the right
print(example.rstrip())

#Strip whitespace from the left
print(example.lstrip())

#Rewrite old variable without whitespace
example = example.rstrip().lstrip()
print(example)
