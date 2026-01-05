# 10-2
# Learning C
from pathlib import Path

path = Path('learning_python.txt')

# reading the contents of the file
content = path.read_text()
content = content.rstrip()

# print content after replacing
print("\n")
print(content)

# print content after replacing
content = content.replace('Python', 'C')
print("\n")
print(content)