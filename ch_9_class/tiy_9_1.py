# ### 9-1 & 9-2
# class Restaurant:
#     """A simple attempt to model a restaurant."""

#     def __init__(self, restaurant_name, cuisine_type):
#         """Initialize name and cuisine attributes."""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         """Display info about restaurant."""
#         print(f"\nRestaurant name: {self.restaurant_name}")
#         print(f"Cuisine type: {self.cuisine_type}")
    
#     def open_restaurant(self):
#         """Display if open."""
#         print(f"Restaurant {self.restaurant_name} is open.")

# restaurant = Restaurant('Bhandari', 'Mughlai')
# print(f"\nName of the restaurant: {restaurant.restaurant_name}")
# print()
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# restaurant_1 = Restaurant('moti mahal', 'mughlai')
# restaurant_1.describe_restaurant()

# restaurant_2 = Restaurant('SRS', 'south indian')
# restaurant_2.describe_restaurant()

# restaurant_3 = Restaurant('Sher-e-punjab', 'afghan')
# restaurant_3.describe_restaurant()

# ### 9-3
# class User:
#     """An attepmt to model a user profile."""

#     def __init__(self, first_name, last_name, username, age, field):
#         """Initialize user's name and other attributes."""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.field = field
#         self.username = username
#         self.fullname = f"{self.first_name.title()} {self.last_name.title()}"
    
#     def describe_user(self):
#         """Describe user information."""

#         print("\nSummary of user's information is: ")
#         print(f"username: {self.username} \nUser's name: {self.fullname.title()}")
#         print(f"User's age: {self.age}")
#         print(f"User's field of work: {self.field.title()}")
    
#     def greet_user(self):
#         """Personalised greeting for user."""
#         print(f"Hello {self.fullname.title()}, Welcome!")

# user_1 = User('shivanie', 'j', 'viku', 8, 'data science')
# user_1.describe_user()
# user_1.greet_user()

# user_2 = User('divyansh', 'j', 'divu', 32, 'law')
# user_2.describe_user()
# user_2.greet_user()