### 6-4
# glossary = {
#     'word wrap': 'makes code in editor appear only in the visible space.',
#     'immutable': 'cannot change',
#     'tuple': 'immutable lists',
#     'looping': 'repetition task',
#     'elif': 'part of if-elif-else conditional construct in pyhton',
# }
## Earlier version
# print(f"I learnt about Word Wrap which means {glossary['word wrap']}.")
# print(f"I learnt about immutable which means {glossary['immutable']}.")
# print(f"I learnt about tuple which means {glossary['tuple']}.")
# print(f"I learnt about looping which means {glossary['looping']}.")
# print(f"I learnt about elif which means {glossary['elif']}.")

## Refined version looping through the dictionary
# for key, value in glossary.items():
#     print(f"I learned about {key}, which implies {value}.")

# ### 6-5
# rivers = {
#     'nile': 'egypt',
#     'ganga': 'india',
#     'brahmaputra': 'china',
# }

# for river, country in rivers.items():
#     print(f"The {river.title()} runs through {country.title()}.")

# print("\nNames of the rivers:")
# for river in rivers:
#     print(river.title())

# print("\nCountries included:")
# for country in rivers.values():
#     print(country.title())

# ### 6-6
# favorite_languages = {
# 'jen': 'python',
# 'sarah': 'c',
# 'edward': 'rust',
# 'phil': 'python',
# }
# people = ['eden', 'adam', 'ada', 'thomas', 'sarah', 'jen']
# for person in people:
#     if person in favorite_languages.keys():
#         print(f"{person.title()}, Thanks for responding.")
#     else:
#         print(f"Please take the poll, {person.title()}.")