from pathlib import Path
import json

number = input("Enter your favorite number: ")
contents = json.dumps(number)
path = Path('favorite_number.json')
path.write_text(contents)