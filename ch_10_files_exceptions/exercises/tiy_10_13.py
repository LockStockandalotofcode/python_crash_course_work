# remember_me.py extended to dictionary from single string information about the user

from pathlib import Path
import json

path = Path('user_info.json')

# input prompt
username = input("Enter your username: ")
age = input("Enter your age: ")
full_name = input("Enter your full name: ")

# form dictionary of data
user_information = {
    'username': username,
    'age': age,
    'full_name': full_name,
}

# save dictionary into file
contents = json.dumps(user_information)
path.write_text(contents)

# read user_info file
contents_2 = path.read_text()
user_informations_2 = json.loads(contents_2)

# print summary of user_info file
print("\nPrinting information about user:")
for k, v in user_informations_2.items():
    print(f"-about {k} : {v}.")