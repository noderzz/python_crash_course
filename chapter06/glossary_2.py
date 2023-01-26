'''
Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionarys keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.
'''
glossary = {
    'variable':'An abstract storage location paired with an associated symbolic name.',
    'dictionary':'An associative array, map, symbol table, or dictionary is an abstract data type that stores a collection of pairs, such that each possible key appears at most once in the collection.',
    'tuple':'An ordered sequence of elements that is immutable.',
    'function':'"Self contained" modules of code that accomplish a specific task.',
    'iterable':'An object which can be looped over or iterated over with the help of a for loop.',
}

for value,definition in glossary.items():
    if value[0].lower() not in ["a","e","i","o","u"]:
        print(f"A {value} is: \n\t{definition}")
    else:
        print(f"An {value} is: \n\t{definition}")
