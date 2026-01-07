from pathlib import Path

path = Path('/Users/shivanie/Desktop/python_work/pcc_3e-main/chapter_10/reading_from_a_file/pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

# print(f"{pi_string[:52]}...")
# print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birtday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
