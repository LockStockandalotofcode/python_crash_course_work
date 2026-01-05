# ### 10-6
# number_1 = input("Enter first number: ")
# number_2 = input("Enter second number: ")

# # putting int conversion of input strings since ValueError can be produced during this step as well
# try:
#     number_1 = int(number_1)
#     number_2 = int(number_2)
#     print(int(number_1) + int(number_2))
# except ValueError:
#     print("You can only add two numbers, not strings.")

### 10-7 
prompt = "Enter 2 numbers to be added:"
prompt += "\n(enter 'q' to end.) "


while True:
    print("\n")
    print(prompt)
    number_1 = input("Enter first number: ")
    if number_1 == 'q':
        break

    number_2 = input("Enter second number: ")
    if number_2 == 'q':
        break

    try:
        number_1 = int(number_1)
        number_2 = int(number_2)
        print(int(number_1) + int(number_2))
    except ValueError:
        print("You can only add two numbers, not strings.")
