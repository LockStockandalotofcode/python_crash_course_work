#### Numbers
# # Exponents
# print(3 ** 3)
# # underscores in numbers to make large numbers(both integers and floats) more readable
# universe_age = 14_000_000_000
# print(universe_age)
# # multiple assignment
# x, y, z = 0, 0,4
# print(x, y, z)
# # Constants - custom to use all capitals as variable name to indicate a constant
# MAX = 500

# ### The Zen of Python
# import this

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

###### Chapter 4 working with lists
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)
#     print(f"{magician.title()} that was a great trick.")

# squares = []
# for value in range(1, 11):
#     squares.append(value ** 2)
# print(squares)

# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits), max(digits), sum(digits))

# squares = [value**2 for value in range(1, 11)]
# print(squares)

# slicing a list
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# print(players[-3:]) # elements starting with last 3rd element until the very end since second index is not specified
# print(players[-3:-2])
# looping through a slice
# print("first three players on my team")
# for player in players[:3]:
#     print(player.title())

# copying a list
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]

# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print("My fav foods are: ")
# print(my_foods)

# print("\nMy friend's fav foods are: ")
# print(friend_foods)

# setting friend_foods = my_foods does not create separate lists
# then, indeed both variables friend_foods and my_foods point to the same list

#### tuples
# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# dimensions[0] = 250 # produces error since tuples are immutable

# # single element tuple
# my_t = (3,)

# looping through a tuple
# for dimension in dimensions:
    # print(dimension)

# writing over a tuple
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)

# dimensions = (400, 10)
# print("new dimensions:")
# for dimension in dimensions:
#     print(dimension)
# # since reassigning a variable is valid

