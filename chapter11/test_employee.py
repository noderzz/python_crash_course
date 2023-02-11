"""
Write a class called Employee. The __init__() method should take in a first name, a last name, and an annual salary, and store each of these as attributes. Write a method called give_raise() that adds $5,000 to the annual salary by default but also accepts a different raise amount.

Write a test file for Employee with two test functions, test_give_default_raise() and test_give_custom_raise(). Write your tests once without using a fixture, and make sure they both pass. Then write a fixture so you don’t have to create a new employee instance in each test function. Run the tests again, and make sure both tests still pass.
"""
from employee import Employee

def test_give_default_raise():
    """Test if the default raise would work."""
    test_employee = Employee('Bob','Smith', 50_000)
    old_salary = test_employee.salary
    test_employee.give_raise()
    assert test_employee.salary == old_salary + 5000

def test_give_custom_raise():
    """Test if the default raise would work."""
    test_employee = Employee('Bob','Smith', 50_000)
    old_salary = test_employee.salary
    test_employee.give_raise(7500)
    assert test_employee.salary == old_salary + 7500
