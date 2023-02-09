from pathlib import Path

path = Path("chapter10/alice.txt")
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file path {path} does not exist.")