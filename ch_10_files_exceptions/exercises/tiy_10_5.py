from pathlib import Path

path = Path('guest_book.txt')

prompt = "Enter your name: "
prompt += "(enter 'q' to end this process.) "
guest_names = ""

while True:
    name = input(prompt)
    if name == 'q':
        break
    else:
        guest_names += name + "\n"

path.write_text(guest_names)