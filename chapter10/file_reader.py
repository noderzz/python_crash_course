from pathlib import Path

path = Path('chapter10/pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)