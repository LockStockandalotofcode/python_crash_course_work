# ### 8-12
# def sandwiches(*items):
#     print("\nEverything that's going to be on the sandwich: ")

#     for item in items:
#         print(f"- {item.title()}")

# sandwiches('ham')
# sandwiches('bacon', 'egg', 'ham')
# sandwiches('ketchup', 'ham')

# ### 8-13
# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile(
#     'Shivanie',
#     'J',
#     location='Hyderabad',
#     field='Data Science')
# print(user_profile)

# ### 8-14
# def make_car(manufacturer, model_name, **car_info):
#     car_info['manufacturer'] = manufacturer
#     car_info['model name'] = model_name
#     return car_info

# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)