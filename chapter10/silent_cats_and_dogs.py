#Modify your except block in Exercise 10-7 to fail silently if either file is missing.
from pathlib import Path

def read_file(path):
    path = Path(path)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"The contents of the {path} file are:\n{contents}")

read_file("chapter10/cats.txt")
print("\n")
read_file("chapter10/dogs.txt")
print("\n")
read_file("chapter10/lizards.txt")