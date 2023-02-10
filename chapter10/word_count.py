from pathlib import Path

def word_count(path):
    """Count the approximate number of words in a file."""
    path = Path("chapter10/alice.txt")
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file path {path} does not exist.")
    else:
        # Count the approximate number of words in theA file:
        words = contents.split()
        num_words = len(words)
        print(f"The file '{path}' has about {num_words} words.")

path = Path('chapter10/alice.txt')
word_count(path)