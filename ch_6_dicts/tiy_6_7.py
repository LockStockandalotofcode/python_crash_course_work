### 6-7
# anshu_dict = {
#     'first_name': 'divyansh',
#     'last_name': 'jangra',
#     'age': 25,
#     'city': 'delhi',
# }

# print(f"About my brother, {anshu_dict['first_name'].title()} {anshu_dict['last_name'].title()} who is {anshu_dict['age']} years old and lives in {anshu_dict['city'].title()}.")

# person1 = {
#     'name': 'viku',
#     'age': 25
# }
# person2 = {
#     'name': 'vinu',
#     'age':22
# }
# people = [person1, person2]

# for person in people:
#     print(f"Hi {person['name'].title()}, you're {person['age']} yrs old.")

# ### 6-8
# pet_1 = {
#     'name': 'robbie',
#     'breed': 'german shepherd',
# }
# pet_2 = {
#     'name': 'vanilla',
#     'breed': 'shih tzu',
# }
# pet_3 = {
#     'name': 'babur',
#     'breed': 'St. Bernard'
# }
# pets = [pet_1, pet_2, pet_3]

# for pet in pets:
#     print(f"The pet named {pet['name'].title()} is a {pet['breed'].title()} breed.")

# ### 6-9
# favorite_places = {
#     'dada':['dahola', 'jind', 'luhari'],
#     'dad':['ladakh', 'jind', 'hyderabad'],
#     'me':['dalhousie', 'chamba', 'mcleodganj'],
# }
# for person, places in favorite_places.items():
#     print(f"\nSome of the favorite places of {person.title()} are:")

#     for place in places:
#         print(f"\t{place.title()}")

# ### 6-8, 6-10 skipping because its mostly the same as 6-7

# ### 6-9
# cities = {
#     'istanbul': {
#         'country': 'turkey',
#         'fact': 'capital city of Turkey',
#     },

#     'delhi': {
#         'country': 'india',
#         'fact': 'capital city of India',
#     },

#     'dalhousie': {
#         'country': 'india',
#         'fact': 'situated in mountains',
#     },

# }

# for city, city_info in cities.items():
#     print(f"\nCity: {city.title()}")
#     country = city_info['country'].title()
#     fact = city_info['fact']

#     print(f"\tPart of country: {country}")
#     print(f"\tAn interesting fact about the city is that it is {fact}.")