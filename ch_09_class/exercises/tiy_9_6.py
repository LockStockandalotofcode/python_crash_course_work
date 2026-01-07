# ### 9-6
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

# class IceCreamStand(Restaurant):
#     """Represent features of a restaurant, specific to an ice cream stand."""
#     def __init__(self, restaurant_name, cuisine_type):
#         """
#         Inittialize attributes of the parent class.
#         Then initialize attributes specific to an ice cream stand.
#         """
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = []
    
#     def display_flavors(self):
#         """Display list of ice cream flavors."""
#         if self.flavors:
#             print("Ice ceam flavors:")
#             for flavor in self.flavors:
#                 print(flavor)

# ice_cream_1 = IceCreamStand('Amul parlor', 'dessert')
# ice_cream_1.describe_restaurant()
# ice_cream_1.flavors = ['vanilla', 'choco']
# ice_cream_1.display_flavors()

# ### 9-7
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
#         print(f"User's field of work: {self.field.title()}\n")
    
#     def greet_user(self):
#         """Personalised greeting for user."""
#         print(f"Hello {self.fullname.title()}, Welcome!\n")

# class Admin(User):
#     """Represent features of a user, specific to an admin."""

#     def __init__(self, first_name, last_name, username, age, field):
#         """
#         Initialize attributes of parent class.
#         Then initialize attributes specific to admin.
#         """
#         super().__init__(first_name, last_name, username, age, field)
#         self.privileges = []

#     def show_privileges(self):
#         """Display list of privileges."""
#         if self.privileges:
#             print("List of Administrator's set of privileges:")
#             for privilege in self.privileges:
#                 print(privilege)
#             print("\n")

# admin_1 = Admin('shivanie', 'j', 'viku', 8, 'data science')
# admin_1.describe_user()
# admin_1.greet_user()
# admin_1.privileges = ['can add post', 'can ban user', 'can delete any member']
# admin_1.show_privileges()

### 9-8
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
#         print(f"User's field of work: {self.field.title()}\n")
    
#     def greet_user(self):
#         """Personalised greeting for user."""
#         print(f"Hello {self.fullname.title()}, Welcome!\n")

# class Privileges:
#     """A simple attempt to model privileges for an Admin"""

#     def __init__(self, privileges=[]):
#         """Initialize attributes of privileges class."""
#         self.privileges = privileges
    
#     def show_privileges(self):
#         """Display list of privileges."""
#         if self.privileges:
#             print("List of Administrator's set of privileges:")
#             for privilege in self.privileges:
#                 print(privilege)
#             print("\n")

# class Admin(User):
#     """Represent features of a user, specific to an admin."""

#     def __init__(self, first_name, last_name, username, age, field):
#         """
#         Initialize attributes of parent class.
#         Then initialize attributes specific to admin.
#         """
#         super().__init__(first_name, last_name, username, age, field)
#         self.privileges = Privileges()

# admin_1 = Admin('shivanie', 'j', 'viku', 8, 'data science')
# admin_1.describe_user()
# admin_1.greet_user()
# admin_1.privileges = Privileges(['can add post', 'can ban user', 'can delete any member'])
# admin_1.privileges.show_privileges()

### 9-9
# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """ Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         """
#         Set the odometere reading to a given value.
#         Reject the change if attempted to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer.")
    
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles

# class Battery:
#     """A simple attempt to model a battery for an electric car."""

#     def __init__(self, battery_size=40):
#         """Inititalize the battery's attributes."""
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kWh battery.")

#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#         if self.battery_size == 40:
#             range = 150
#         elif self.battery_size == 65:
#             range = 225
        
#         print(f"This car can go about {range} miiles on a full charge.")
    
#     def upgrade_battery(self):
#         """Upgrades battery to 65, if not already."""
#         if self.battery_size != 65:
#             self.battery_size = 65

# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""

#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery = Battery()

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()

# # upgrade battery
# my_leaf.battery.upgrade_battery()
# # call get range once again
# my_leaf.battery.get_range()