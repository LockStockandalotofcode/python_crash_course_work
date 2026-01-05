### 8-15
## printing_models.py

# Start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Simulate printing each design, until none are left.
# # Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)
    
# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

# functions to replace above blocks

# import printing_functions as pf

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# pf.print_models(unprinted_designs, completed_models)
# pf.show_completed_models(completed_models)

# ### 8-16
# from city import *

# pair_1 = city_country('istanbul', 'turkey')
# pair_2 = city_country('delhi', 'india')
# pair_3 = city_country('las vegas', 'america')

# print(pair_1)
# print(pair_2)
# print(pair_3)