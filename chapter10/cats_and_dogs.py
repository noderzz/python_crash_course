#Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block executes properly.
from pathlib import Path

def read_file(path):
    path = Path(path)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"I'm sorry, the file {path} doesn't appear to exist.")
    else:
        print(f"The contents of the {path} file are:\n{contents}")

read_file("chapter10/cats.txt")
print("\n")
read_file("chapter10/dogs.txt")
print("\n")
read_file("chapter10/lizards.txt")