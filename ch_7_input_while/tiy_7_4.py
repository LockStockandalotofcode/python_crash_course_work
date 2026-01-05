# ### 7-4
# prompt = "\nEnter pizza toppings you wish to add."
# prompt += "(Enter 'quit' to end the program.) "

# topping = ''
# while topping != 'quit':
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f"Adding {topping} topping.")

# ### 7-5 # used flag and a break
# prompt = "\nEnter your age: "
# prompt += "(Enter 'quit' to end the program.)"

# active = True #Flag
# while active:
#     age = input(prompt)
#     if age == 'quit':
#         active = False
#         break
    
#     age = int(age)
#     if age < 3:
#         print("Your ticket is free.")
#     elif age < 12:
#         print("YOur ticket costs $10.")
#     else:
#         print("Your ticket costs $15.")

### 7-6

# ## 7-4 (1)
# prompt = "\nEnter pizza toppings you wish to add."
# prompt += "(Enter 'quit' to end the program.) "

# topping = ''
# while topping != 'quit':
#     topping = input(prompt)
#     if topping == 'quit':
#         break

#     print(f"Adding {topping} topping.")

# ## 7-4 (2)
# prompt = "\nEnter pizza toppings you wish to add."
# prompt += "(Enter 'quit' to end the program.) "

# active = True
# while active:
#     topping = input(prompt)

#     if topping == 'quit':
#         active = False
#     else:
#         print(f"Adding {topping} topping.")

## 7-4 (3)
# prompt = "\nEnter pizza toppings you wish to add."
# prompt += "(Enter 'quit' to end the program.) "

# while True:
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f"Adding {topping} topping.")
#     else:
#         break

### 7-7 # already done 