"""
Type hints
"""

# python < 3.10 needs Union
# python >= 3.10 can use the pipe operator `|`
from typing import Union


def simple_calculator_py39_and_lower(number1: Union[int, float],
                                     number2: Union[int, float],
                                     operation: str = '+') -> float:
    """Calculate the addition or subtraction of two numbers."""
    if not all([isinstance(i, (int, float)) for i in (number1, number2)]):
        raise ValueError("The input numbers must be of type int or float.")

    if operation == '+':
        return float(number1 + number2)
    elif operation == '-':
        return float(number1 - number2)
    else:
        raise ValueError("The `operation` must be either '+' or '-'.")


def simple_calculator_py310_and_higher(number1: int | float,
                                       number2: int | float,
                                       operation: str = '+') -> float:
    """Calculate the addition or subtraction of two numbers."""
    if not all([isinstance(i, (int, float)) for i in (number1, number2)]):
        raise ValueError("The input numbers must be of type int or float.")

    if operation == '+':
        return float(number1 + number2)
    elif operation == '-':
        return float(number1 - number2)
    else:
        raise ValueError("The `operation` must be either '+' or '-'.")


if '__main__' == __name__:
    print(simple_calculator_py39_and_lower(2, 3))

    print(simple_calculator_py310_and_higher(2, 3))
