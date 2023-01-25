'''
A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
'''
glossary = {
    'variable':'An abstract storage location paired with an associated symbolic name.',
    'dictionary':'An associative array, map, symbol table, or dictionary is an abstract data type that stores a collection of pairs, such that each possible key appears at most once in the collection.',
    'tuple':'An ordered sequence of elements that is immutable.',
    'function':'"Self contained" modules of code that accomplish a specific task.',
    'iterable':'An object which can be looped over or iterated over with the help of a for loop.',
}
print("A Variable is:")
print(f"\t{glossary['variable']}")
print("A Dictionary is:")
print(f"\t{glossary['dictionary']}")
print("A Tuple is:")
print(f"\t{glossary['tuple']}")
print("A Function is:")
print(f"\t{glossary['function']}")
print("An Iterable is:")
print(f"\t{glossary['iterable']}")