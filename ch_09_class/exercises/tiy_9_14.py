# 9-14 Lottery

from random import choice

available  = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e']

winner_list = []
# randomly select 4 digits and 1 letter and form winner list
# for value in range(0, 4):
    # chosen = choice(available)
    # winner_list.append(chosen)

# # Print result
# print(f"Any ticket matching {winner_list} wins a prize.")

# 9-15 Lottery analysis
my_ticket = ['a', 'b', '6', '3']

count = 0

while my_ticket != winner_list:
    winner_list = []

    for value in range(0, 4):
        chosen = choice(available)
        winner_list.append(chosen)

    count += 1

print(f"It took {count} times for the loop generate the ticket {winner_list}.")