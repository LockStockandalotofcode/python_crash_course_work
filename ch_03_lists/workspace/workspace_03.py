
# ### Lists
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[-1]) # to access last element in a list
# print(bicycles[-2]) # above convention extends to other negative indices as well; for e.g. -2 returns last 2nd element
# message = f"My first bicycle was a {bicycles[0].title()}."
# print(message)

# bicycles[0] = 'montra'
# print(bicycles)
# bicycles.append('trek')
# print(bicycles)
# bicycles.insert(2, 'atlas')
# print(bicycles)

# # removing an item/element from a list: by index (using del) or by value (using pop())
# del bicycles[2]
# print(bicycles)

# last_owned = bicycles.pop()
# print('--')
# print(f'The last bicycle I owned was a {last_owned.title()}.')
# first_owned = bicycles.pop(0)
# #print(f'The first bicycle I owned was a {first_owned.title()}.')
# print(f"The first bike I owned was a {first_owned.title()}.")
# print(bicycles)

# too_expensive = 'redline'
# bicycles.remove(too_expensive)
# print(bicycles)
# print(f"\nA {too_expensive.title()} is too expensive for me.")
# # remove() method only deletes the first occurence of an element

# ### permanent sorting using sort()
# cars = ['bmw', 'audi', 'toyota', 'isuzu']
# cars.sort()
# print(cars)
# # permanent reverse sort
# cars.sort(reverse = True)
# print(cars)

# ### temporary sort using sorted()
# cars = cars = ['bmw', 'audi', 'toyota', 'isuzu']
# print("Here's the original list:")
# print(cars)
# print("\nHere is the sorted list:")
# print(sorted(cars))
# print("\nHere's the original list again:")
# print(cars)

### to sort a list in reverse-chronological order not necessarily reverse-alphabetically
# cars.reverse()
# print(cars)
# print(len(cars))

### indexing errors
# turkey_cities = ['Istanbul', 'Antalya', 'Bolu', 'Yaslihan']
# print(turkey_cities[3])
