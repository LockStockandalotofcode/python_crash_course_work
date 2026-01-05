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

## RETURN VALUE
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
print(get_formatted_name('jimi', 'hendrix'))