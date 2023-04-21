"""
# Checking that our custom error is raised in a test.

See "testing_pytest.py" for a first introduction.

See README.md for details on installation.

Remember Arrange, Act, Assert

"""

import pytest


class BadOperationError(ValueError):
    pass


class NotANumberError(ValueError):
    pass


def simple_calculator(number1, number2, operation='+'):
    """Calculate the addition or subtraction of two numbers."""
    if not all([isinstance(i, (int, float)) for i in (number1, number2)]):
        raise NotANumberError("The input numbers must be of type int or float.")

    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    else:
        raise BadOperationError("The `operation` must be either '+' or '-'.")


# let's test the custom error

def test_simple_calculator_bad_numbers():
    """Test the number arguments."""
    # arrange
    number1 = "five"
    number2 = 2
    operation = '+'

    # act (here, our 'assert' step is the error check)
    with pytest.raises(NotANumberError):
        simple_calculator(number1, number2, operation=operation)


def test_simple_calculator_bad_operation():
    """Test the number arguments."""
    # arrange
    number1 = 7
    number2 = 2
    operation = '/'

    # act (here, our 'assert' step is the error check)
    with pytest.raises(BadOperationError):
        simple_calculator(number1, number2, operation=operation)

    # you may ask, how do I know that the correct ValueError is being raised?
    # For that, we must cover errors and custom errors!
