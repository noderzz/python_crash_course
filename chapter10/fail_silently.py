from pathlib import Path

def word_count(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        # Count the approximate number of words in theA file:
        words = contents.split()
        num_words = len(words)
        print(f"The file '{path}' has about {num_words} words.")

path = Path('chapter10/wookie.txt')
word_count(path)