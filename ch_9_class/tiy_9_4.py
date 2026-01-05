### 9-4
# class Restaurant:
#     """A simple attempt to model a restaurant."""

#     def __init__(self, restaurant_name, cuisine_type):
#         """Initialize name and cuisine attributes."""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         """Display info about restaurant."""
#         print(f"\nRestaurant name: {self.restaurant_name}")
#         print(f"Cuisine type: {self.cuisine_type}")
    
#     def open_restaurant(self):
#         """Display if open."""
#         print(f"Restaurant {self.restaurant_name} is open.")
    
#     def set_number_served(self, updated_served):
#         """Set the number of customers who have been served."""
#         self.number_served = updated_served
    
#     def increment_number_served(self, increment):
#         """Increment the number of customers served."""
#         self.number_served += increment

# print("\n")

# restaurant = Restaurant('moti mahal', 'mughlai')
# print(f"Number of customers served: {restaurant.number_served}")
# # restaurant.number_served = 40
# # print(f"Number of customers served: {restaurant.number_served}")
# # restaurant.set_number_served(40)
# # print(f"Number of customers served: {restaurant.number_served}")

# restaurant.increment_number_served(50)
# print(f"Number of customers served: {restaurant.number_served}")

# ### 9-5
# class User:
#     """An attepmt to model a user profile."""

#     def __init__(self, first_name, last_name, username, age, field, ):
#         """Initialize user's name and other attributes."""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.field = field
#         self.username = username
#         self.fullname = f"{self.first_name.title()} {self.last_name.title()}"
#         self.login_attempts = 0
    
#     def describe_user(self):
#         """Describe user information."""

#         print("\nSummary of user's information is: ")
#         print(f"username: {self.username} \nUser's name: {self.fullname.title()}")
#         print(f"User's age: {self.age}")
#         print(f"User's field of work: {self.field.title()}")
    
#     def greet_user(self):
#         """Personalised greeting for user."""
#         print(f"Hello {self.fullname.title()}, Welcome!")
    
#     def increment_login_attempts(self):
#         """Increment the value of login attempts by 1."""
#         self.login_attempts += 1
    
#     def reset_login_attempts(self):
#         """ Reset the login attempts to 0."""
#         self.login_attempts = 0

# user_1 = User('shivanie', 'j', 'viku', 8, 'data science')

# user_1.increment_login_attempts()
# num_attempts = user_1.login_attempts
# print(f"Number of login attempts: {num_attempts}")

# user_1.increment_login_attempts()
# num_attempts = user_1.login_attempts
# print(f"Number of login attempts: {num_attempts}")

# user_1.increment_login_attempts()
# num_attempts = user_1.login_attempts
# print(f"Number of login attempts: {num_attempts}")

# user_1.increment_login_attempts()
# num_attempts = user_1.login_attempts
# print(f"Number of login attempts: {num_attempts}")

# user_1.increment_login_attempts()
# num_attempts = user_1.login_attempts
# print(f"Number of login attempts: {num_attempts}")

# user_1.reset_login_attempts()
# num_attempts = user_1.login_attempts
# print(f"Number of login attempts: {num_attempts}")
