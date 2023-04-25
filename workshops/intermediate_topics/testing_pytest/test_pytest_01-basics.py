"""
See README.md
"""


# we write tests by simply creating a function that starts with "test"
# here is a simple function
# (this function is usually not in the same file as the test functions!)

def add_some_numbers(number1, number2):
    addition = number1 + number2
    return addition


# we test this function with a test function like so:

def test_add_some_numbers_int():
    """Test the addition of two integers."""
    # arrange
    number1 = 1
    number2 = 2
    expected_value = 3

    # act
    addition = add_some_numbers(number1, number2)

    # assert
    assert addition == expected_value


# now run `pytest workshops/intermediate_topics/testing_pytest/testing_pytest_01-basics.py`
# or use PyCharm's "Run tests" option
