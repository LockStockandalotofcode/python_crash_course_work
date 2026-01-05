### 9-13
from random import randint
class Die:
    """A simple attempt to model a die."""

    def __init__(self, sides=6):
        """Initialise the attributes to class Die."""
        self.sides = sides
    
    def roll_die(self):
        """ Method to print a random number between 1 and number of sides of die. """
        roll = randint(1, self.sides)
        print(roll)

my_die = Die(6)
print("\nRolling a 6-sided die:")
for value in range(0, 5):
    my_die.roll_die()