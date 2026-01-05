"""A class that represents an Admin and its privileges."""

from user_only import User

class Privileges:
    """A simple attempt to model privileges for an Admin"""

    def __init__(self, privileges=[]):
        """Initialize attributes of privileges class."""
        self.privileges = privileges
    
    def show_privileges(self):
        """Display list of privileges."""
        if self.privileges:
            print("List of Administrator's set of privileges:")
            for privilege in self.privileges:
                print(privilege)
            print("\n")

class Admin(User):
    """Represent features of a user, specific to an admin."""

    def __init__(self, first_name, last_name, username, age, field):
        """
        Initialize attributes of parent class.
        Then initialize attributes specific to admin.
        """
        super().__init__(first_name, last_name, username, age, field)
        self.privileges = Privileges()
