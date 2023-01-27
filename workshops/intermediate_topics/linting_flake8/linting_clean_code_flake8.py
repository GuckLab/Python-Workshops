"""
# Clean code & Linting
In this workshop we will learn to write clean code following Python's PEP8 protocol.

We can "scan" our code for syntax and style problems by linting.

One popular linting tool is the flake8 package.

## Installing flake8

`pip install flake8`

## Using flake8

`flake8 path/to/file.py`

We can also run it on multiple files or directories:

`flake8 path/to/file.py path/to/directory`

"""

# here is an example of some unclean code. flake8 to the rescue!
import numpy as np
def add_some_numbers(number1,
                        number2):
    addition = number1  + number2


    return(addition)

if __name__ == '__main__':

    add_some_numbers(2, 4)




