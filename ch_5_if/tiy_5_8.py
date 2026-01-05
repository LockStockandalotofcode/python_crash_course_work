# usernames = ['admin', 'shizu', 'voofy', 'babur', 'fifu']
## 5-8, 5-9
# if usernames:
#     for username in usernames:
#         if username == 'admin':
#             print("Hello admin, would you like to see a status report?")
#         else:
#             print("Hello Jaden, thank you for logging in again.")
# else:
#     print("We need to find some users.")

## 5-10
# current_users = ['mum', 'dad', 'viks', 'viku', 'voofy', 'bacardi', 'saifi']
# new_users = ['Bacardi', 'saifi', 'jackie', 'oreo', 'bruno']
# copy_current_users = []
# for current_user in current_users:
#     copy_current_users.append(current_user.lower())

# for new_user in new_users:
#     if new_user.lower() in current_users:
#         print(f"{new_user} will need to enter a new username.")
#     else:
#         print(f"{new_user} username is available.")

ordinals = list(range(1, 10))

for ordinal in ordinals:
    if ordinal == 1:
        print("1st")
    elif ordinal == 2:
        print('2nd')
    elif ordinal == 3:
        print("3rd")
    else:
        print(f"{ordinal}th")