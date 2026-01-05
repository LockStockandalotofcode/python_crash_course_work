### 10-4
from pathlib import Path

guest_name = input("Enter your name: ")
path = Path('guest.txt')
path.write_text(guest_name)