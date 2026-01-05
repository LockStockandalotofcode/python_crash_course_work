class Employee:
    """A simple attempt to model an employee profile."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialise attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        """Add raise to annual salary amount."""
        self.annual_salary += raise_amount