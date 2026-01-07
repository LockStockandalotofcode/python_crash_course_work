guests = ['Mummy', 'Viks', 'daddy', 'voofy', 'saifi', 'bacardi']
# 3-4
print(f"Hello {guests[0].title()}, I've planned a dawat for you.")
# 3-5
print(f"{guests[1].title()} can't make it to the dinner because of work commitments.")
guests.remove('Viks')
guests.insert(1, 'Jyoti Aunty') # replacing item Viks with Jyoti Aunty at the same index
# 3-6
print("As I've found a bigger dining table, we'll be inviting more people now.")
print(len(guests))
guests.insert(0, 'nani')
guests.insert(3, 'nana ji')
guests.append('dakshit')
# 3-7
print("Sorry for the inconvenience and earlier messages, there's space for only 2.")
not_invited = guests.pop() # guest 9
print(f"Sorry {not_invited.title()}, you're not invited anymore.")
not_invited = guests.pop() # guest 8
print(f"Sorry {not_invited.title()}, you're not invited anymore.")
not_invited = guests.pop() # guest 7
print(f"Sorry {not_invited.title()}, you're not invited anymore.")
not_invited = guests.pop() # guest 6
print(f"Sorry {not_invited.title()}, you're not invited anymore.")
not_invited = guests.pop() # guest 5
print(f"Sorry {not_invited.title()}, you're not invited anymore.")
not_invited = guests.pop() # guest 4
print(f"Sorry {not_invited.title()}, you're not invited anymore.")
not_invited = guests.pop() # guest 3
print(f"Sorry {not_invited.title()}, you're not invited anymore.")

print(f"Hello {guests[0].title()}, you're still invited.")
print(f"Hello {guests[1].title()}, you're still invited.")

del guests[1]
del guests[0]
print(guests)