"""
# Unit testing with pytest

A unit test is a test on one part of your code. Ideally you are testing a
function or method.
The next level would be system tests that test many aspects of a program together.

We use the popular `pytest` package for testing.

## Why do we need to write tests?

We write tests so that we know that our code works as expected.
With tests we can check that the actual output of our code is what we expect.

## Installing pytest

`pip install pytest`

## Using pytest

`pytest path/to/file.py`

We can also run it on multiple files or directories:

`pytest path/to/directory path/to/file.py`

The tests are usually in a separate directory from the package code.

## Arrange, Act, Assert

The test is split up into:
- Arrange: we set up any variables we eed, including the expected answer.
- Act: Run the code that is being tested.
- Assert: use the python `assert` statement to check if the actual and expected
  output are the same.

"""


# we write tests by simply creating a function that starts with "test"
# here is a simple function

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


# now run `pytest workshops/intermediate_topics/testing_pytest/unit_testing_pytest.py`
