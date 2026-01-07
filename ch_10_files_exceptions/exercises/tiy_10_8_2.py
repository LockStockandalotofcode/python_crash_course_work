### 10-8, 10-9
# read and print cats.txt and dogs.txt files
from pathlib import Path

# read contentf of cats.txt file
path__1 = Path('cats.txt')
# read contentf of dogs.txt file
path__2 = Path('dogs.txt')

# try-except block to catch FileNotFound error 
# filenotfound error arises only once you try to read text from a file
try:
    content__1 = path__1.read_text()
except FileNotFoundError:
    # print(f"The file {path__1} does not exist.")
    pass
else:
    print(f"\nDisplaying contents of {path__1} file: ")
    print(content__1)

try:
    content__2 = path__2.read_text()
except FileNotFoundError:
    # print(f"The file {path__2} does not exist.")
    pass
else:
    print(f"\nDisplaying contents of {path__2} file: ")
    print(content__2)