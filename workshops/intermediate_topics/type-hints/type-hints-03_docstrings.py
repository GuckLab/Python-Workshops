"""
Type hints

What do type-hints change about our docstrings?
"""

# python < 3.10 you need to import annotations (e.g. pipe) operator
# from __future__ import annotations


def simple_calculator_with_typehints(number1: int | float,
                                     number2: int | float,
                                     operation: str = '+') -> float:
    """Calculate the addition or subtraction of two numbers.

    Parameters
    ----------
    number1, number2
        The two numbers input to the calculation.
    operation
        '+' or '-'

    Returns
    -------
    Calculation of the numbers.

    """
    if not all([isinstance(i, (int, float)) for i in (number1, number2)]):
        raise ValueError("The input numbers must be of type int or float.")

    if operation == '+':
        return float(number1 + number2)
    elif operation == '-':
        return float(number1 - number2)
    else:
        raise ValueError("The `operation` must be either '+' or '-'.")


def simple_calculator_no_typehints(number1,
                                   number2,
                                   operation='+'):
    """Calculate the addition or subtraction of two numbers.

    Parameters
    ----------
    number1, number2 : int or float
        The two numbers input to the calculation.
    operation : str
        '+' or '-'

    Returns
    -------
    float
        Calculation of the numbers.

    """
    if not all([isinstance(i, (int, float)) for i in (number1, number2)]):
        raise ValueError("The input numbers must be of type int or float.")

    if operation == '+':
        return float(number1 + number2)
    elif operation == '-':
        return float(number1 - number2)
    else:
        raise ValueError("The `operation` must be either '+' or '-'.")
