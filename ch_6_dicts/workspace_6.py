# alien_0 = {'color' : 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])

# print(alien_0)
# alien_0['x_pos'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5

# alien_0['color'] = 'yellow'
# print(alien_0)
# print(f"The alien is now {alien_0['color']}.")

# alien_0 = {'x_pos':0, 'y_pos':0, 'speed':'medium'}
# print(f"Original position: {alien_0['x_pos']}")

# # Move the alien to the right.
# # Determine how far to move the alien based on its current speed.
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # This must be a false alien
#     x_increment = 3

# # The new position is the old position plus the increment.
# alien_0['x_pos'] = alien_0['x_pos'] + x_increment

# print(f"New position: {alien_0['x_pos']}")

# # removing key-value pairs
# alien_0 = {'color' : 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)

# # dictionary of similar objects
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# # using get()
# alien_0 = {'color': 'green', 'speed': 'slow'}
# point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)

# ### looping through a dictionary
# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }
# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")

# favorite_languages = {
# 'jen': 'python',
# 'sarah': 'c',
# 'edward': 'rust',
# 'phil': 'python',
# }
## looping through all key-value pairs
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")
## Looping through all keys: default behaviour when looping a dictionary when not specified particular method like items(), or keys() or values()
# for name in favorite_languages.keys():
#     print(name.title())

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}.")

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}.")

# building a set: stores unique elements, no repetition, order of items not retained
# languages = {'python', 'rust', 'python', 'c'}
# print(languages)

### NESTING
## list of dictionaries
# alien_0 = {
#     'color': 'green',
#     'points': 5,
# }
# alien_1 = {
#     'color': 'yellow',
#     'points': 10,
# }
# alien_2 = {
#     'color': 'red',
#     'points': 15,
# }

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

## realistic example
# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'slow',
    }
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created thus far.
print(f"Total number of aliens created: {len(aliens)}")