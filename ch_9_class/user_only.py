"""A class that represents a user only."""

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
