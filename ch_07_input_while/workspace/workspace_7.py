### USER INPUT
# message = input("Tell me something, and I will repeat after you: ")
# print(message)

# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")

# prompt = "If you share your name, we can personalize the messages for you."
# prompt += "\nWhat is your name? "
# name = input(prompt)
# print(f"\nHello, {name}!")

# age = int(input("How old are you? "))
# if age > 18:
#     print(age)

# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")

# ### WHILE LOOP
# current_num = 1
# while current_num <= 5:
#     print(current_num)
#     current_num += 1

# ## FLAG
# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = input(prompt)
    
#     if message == 'quit':
#         active = False
#     else:
#         print(f"\t{message}")

# ## BREAK
# prompt = "\n\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter quit() once you are finished.) "

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"\nI'd love to go to {city.title()}!")

# ## CONTINUE
# current_num = 0
# while current_num < 10:
#     current_num += 1
#     if current_num % 2 == 0:
#         continue

#     print(current_num)

# ## AVOIDING INFINITE LOOPS
# x = 1
# while x <= 5:
#     print(x)

# ### USING WHILE LOOPS WITH LISTS AND DICTIONARIES
# # Starting with users that need to be verified, and an empty list to hold confirmed users.
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# # Verify each user until there are no more unconfirmed users.
# # Move each verified user into the list of confirmed users.
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# # Display all confirmed users.
# print("\nTHe following users have been confirmed: ")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# ### REMOVING ALL INSTANCES OF A VALUE FROM A LIST

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

# ### filling dictionary with user input
# responses = {}
# # Set a flag to indicate that polling is still active.
# polling_active = True

# while polling_active:
#     # Prompt for the person's name and response.
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")

#     # Store the responses in the dictionary.
#     responses[name] = response # name: key, response: value

#     # Find out if anyone else is going to take the poll.
#     repeat = input("Would you like someone else to take the poll? (yes/ no) ")
#     if repeat == 'no':
#         polling_active = False

# # Polling is completet. Show the results.
# print("\n---Poll Results---")
# for name, response in responses.items():
#     print(f"{name.title()} would like to climb {response.title()}.")
