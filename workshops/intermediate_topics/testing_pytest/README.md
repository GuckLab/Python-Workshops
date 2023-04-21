
# Unit testing with pytest

A unit test is a test on one part of your code. Ideally you are testing a
function or method.
The next level would be system tests that test many aspects of a program together.

We use the popular `pytest` package for testing.

## Why do we need to write tests?

We write tests so that we know that our code works as expected.
With tests we can check that the actual output of our code is what we expect.


### Pytest's motto: Arrange, Act, Assert

The test is split up into:
- **Arrange**: we set up any variables we need, including the expected answer.
- **Act**: Run the code that is being tested.
- **Assert**: use the python `assert` statement to check if the actual and expected
  output are the same.

See the examples in the `testing_pytest.py` files.


## Installing pytest

`pip install pytest`

## Using pytest

`pytest path/to/file.py`

We can also run it on multiple files or directories:

`pytest path/to/directory path/to/file.py`

The tests are usually in a separate directory from the package code.


## Related Topics

- See the Errors and Warnings notebook for how to use and create custom errors.
  We test our custom errors in the `testing_pytest_03_custom_error.py` file
- Code Coverage can be used to check how much of your code that your tests cover.
- See the 