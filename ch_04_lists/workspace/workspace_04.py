
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

