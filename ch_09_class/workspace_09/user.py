"""A class that can be used to represent a User."""

class User:
    """An attepmt to model a user profile."""

    def __init__(self, first_name, last_name, username, age, field):
        """Initialize user's name and other attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.field = field
        self.username = username
        self.fullname = f"{self.first_name.title()} {self.last_name.title()}"
    
    def describe_user(self):
        """Describe user information."""

        print("\nSummary of user's information is: ")
        print(f"username: {self.username} \nUser's name: {self.fullname.title()}")
        print(f"User's age: {self.age}")
        print(f"User's field of work: {self.field.title()}\n")
    
    def greet_user(self):
        """Personalised greeting for user."""
        print(f"Hello {self.fullname.title()}, Welcome!\n")

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
