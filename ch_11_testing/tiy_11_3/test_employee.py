import pytest
from employee_class import Employee

@pytest.fixture
def employee():
    """An employee instance object that will be available to all functions."""
    employee = Employee('Aman', 'Singh', 10000)
    return employee

def test_give_default_value(employee):
    """Test that default raise is added to annual salary properly."""
    employee.give_raise()
    assert 15000 == employee.annual_salary

def test_give_custom_raise(employee):
    """Test that custom raise is added to annual salary properly."""
    employee.give_raise(2000)
    assert 12000 == employee.annual_salary