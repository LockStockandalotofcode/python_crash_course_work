from pathlib import Path

path = Path('learning_python.txt')

# reading file method 1
print("\nPrinting first time by reading the entire file: ")
contents_1 = path.read_text()
contents_1 = contents_1.rstrip()
print(contents_1)

# reading the file method 2
print("\nPrinting the second time by looping over each line.")
contents_2 = path.read_text()
# lines = contents_2.splitlines()
for line in contents_2.splitlines():
    print(line)