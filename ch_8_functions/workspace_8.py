# ## simplest function
# def greet_user():
#     """
#     Display a simple greeting.
#     """
#     print("\nHello!")
# 
# greet_user()

# ## with arguments
# def greet_user(username): # parameter : username
#     """ Display a simple greeting."""
#     print(f"\nHello {username.title()}!")

# greet_user('jesse') # argument

# ## RETURN VALUE
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# ## FUNCTION WITH WHILE LOOP
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# # an infinite loop
# while True:
#     print("\nPlease tell me your name: ")
#     print("(Enter 'q' at any time to quit.)")
    
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break

#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
    
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f'\nHello, {formatted_name}!')

# ## PASSING LIST TO FUNCTION
# def greet_users(names):
#     """Print greeting to each user in the list."""
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)

# usernames = ['sarah', 'shiru', 'shizu']
# greet_users(usernames)
