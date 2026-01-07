# ### 7-8
# sandwich_orders = ['club sandwich', 'grilled cheese', 'reuben', 'reuben', 'grilled cheese', 'reuben']
# finished_sandwiches = []

# # Print message for each order.
# for sandwich_order in sandwich_orders:
#     print(f"I made your {sandwich_order.title()} sandwich.")
#     finished_sandwiches.append(sandwich_order)

# # Showing all sandwiches that were made.
# print("\n---All sandwiches made---")
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich.title())

# ### 7-9
# sandwich_orders = ['pastrami','club sandwich', 'grilled cheese', 'pastrami', 'reuben', 'reuben', 'pastrami', 'grilled cheese', 'reuben']
# finished_sandwiches = []

# # Message for shortage of pastrami and removing all occurences of pastrami orders.
# print("The deli has run out of Pastrami.")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# # Print message for each order.
# for sandwich_order in sandwich_orders:
#     print(f"I made your {sandwich_order.title()} sandwich.")
#     finished_sandwiches.append(sandwich_order)

# # Showing all sandwiches that were made.
# print("\n---All sandwiches made---")
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich.title())

# ### 7-10
# responses = {}
# # Set a flag to indicate polling is still active.
# polling_active = True

# while polling_active:
#     # Prompt user to enter data
#     name = input("\nWhat is your name? ")
#     response = input("If you could visit one place in the world, where would you go? ")

#     # store the input data into dictionary
#     responses[name] = response

#     # Find out if anyone else is going to take the poll
#     repeat = input("Would you like someone else to take the poll? (yes/ no) ")
#     if repeat == 'no':
#         polling_active = False

# # Polling is complete. Show the results of poll.
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name.title()} would like to go to {response.title()} someday.")