from pathlib import Path

# path = Path('pi_digits.txt')
# path = Path('/Users/shivanie/Desktop/python_work/text_files/pi_digits.txt')

# contents = path.read_text()
# contents = contents.rstrip()
# method chaining
# contents = path.read_text().rstrip()
# print(contents)

path = Path('pi_digits.txt')
contents = path.read_text()
# lines = contents.splitlines()
for line in contents.splitlines():
    print(line)