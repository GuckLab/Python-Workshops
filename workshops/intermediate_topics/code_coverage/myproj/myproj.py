
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
