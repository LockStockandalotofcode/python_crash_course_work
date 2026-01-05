from pathlib import Path
import json

# path = Path('favorite_number.json')

# # writing to a file
# number = input("Enter your favorite number: ")
# contents = json.dumps(number)
# path = Path('favorite_number.json')
# path.write_text(contents)

# # reading the file
# contents = path.read_text()
# favorite_number = json.loads(contents)

# print(f"I know your favorite number, it's {favorite_number}.")


# path
path = Path('favorite_number.json')
# if file exists : read data
if path.exists():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"I know your favorite number, it's {favorite_number}.")
# if not : prompt user, then write and save data to the file
else:
    favorite_number = input("Enter your favorite number: ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    print(f"We'll remember your favorite number  {favorite_number}, when you come back.")