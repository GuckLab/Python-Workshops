"""
Type hints

Python versions and type-hints
"""

# python < 3.10 you need to import annotations (e.g. pipe) operator
from __future__ import annotations
# python >= 3.10 can use the pipe operator `|` without importing


def simple_calculator(number1: int | float,
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
    print(simple_calculator(2, 3))
