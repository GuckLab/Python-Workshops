
# Code Coverage

You can see how many lines of your code are being tested using Code Coverage.
It goes hand-in-hand with Testing.

For Code Coverage we use the `pytest-cov` pytest plugin or
the `coverage` package (with which you can use PyCharm's "Run 
test with coverage"). This is really nice for visualising which lines were covered
by tests.


## Installing pytest-cov

`pip install pytest-cov`

Details: https://pytest-cov.readthedocs.io/en/latest/

## Using pytest-cov

You must specify what module or package you wish to check coverage for with the
`--cov=myproj` option.

`pytest --cov=myproj path/to/tests`

For our example in this workshop, our code is in the `myproj` folder,
and our tests for that module are in `test_myproj.py` module. So the command
for checking coverage becomes:

`pytest --cov=myproj test_myproj.py`


## Installing coverage

`pip install coverage`


Details: https://coverage.readthedocs.io/en/7.2.3/

## Using coverage

You can run coverage via PyCharm (which is super nice for visualising lines covered).
Just right click on the test file and click "More Run/Debug > Run ... with Coverage".

Or run it via the terminal:

`coverage run -m pytest test_myproj.py`

then to see the report:

`coverage report`
