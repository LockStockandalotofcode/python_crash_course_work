# # importing multiple classes from a module
# from car import Car, ElectricCar

# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# # importing the entire module
# import car

# my_mustang = car.Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())
# my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# importing all classes from a module
from car import Car
from electric_car import ElectricCar 

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
