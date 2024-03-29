"""
# More complicated testing with pytest

See "testing_pytest.py" for a first introduction.

See README.md for details on installation.

Remember Arrange, Act, Assert

Let's write a more complicated function that needs to be tested...

"""

import pytest


def simple_calculator(number1, number2, operation='+'):
    """Calculate the addition or subtraction of two numbers."""
    if not all([isinstance(i, (int, float)) for i in (number1, number2)]):
        raise ValueError("The input numbers must be of type int or float.")

    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    else:
        raise ValueError("The `operation` must be either '+' or '-'.")


# we test this function with several tests:

def test_simple_calculator_addition():
    """Test the addition of two numbers."""
    # arrange
    number1 = 1
    number2 = 2
    operation = '+'
    expected_value = 3

    # act
    calc_val = simple_calculator(number1, number2, operation=operation)

    # assert
    assert calc_val == expected_value


def test_simple_calculator_subtraction():
    """Test the subtraction of two numbers."""
    # arrange
    number1 = 1
    number2 = 2
    operation = '-'
    expected_value = -1

    # act
    calc_val = simple_calculator(number1, number2, operation=operation)

    # assert
    assert calc_val == expected_value


def test_simple_calculator_floats():
    """Test the addition and subtraction of two floats."""
    # arrange
    number1 = 5.5
    number2 = 1.0
    expected_value_add = 6.5
    expected_value_sub = 4.5

    # act
    calc_val_add = simple_calculator(number1, number2, operation='+')
    calc_val_sub = simple_calculator(number1, number2, operation='-')

    # assert
    assert calc_val_add == expected_value_add
    assert calc_val_sub == expected_value_sub


def test_simple_calculator_bad_numbers():
    """Test the number arguments."""
    # arrange
    number1 = "five"
    number2 = 2
    operation = '+'

    # act (here, our 'assert' step is the error check)
    with pytest.raises(ValueError):
        simple_calculator(number1, number2, operation=operation)


def test_simple_calculator_bad_operation():
    """Test the number arguments."""
    # arrange
    number1 = 7
    number2 = 2
    operation = '/'

    # act (here, our 'assert' step is the error check)
    with pytest.raises(ValueError):
        simple_calculator(number1, number2, operation=operation)

    # you may ask, how do I know that the correct ValueError is being raised?
    # For that, we must cover errors and custom errors!
