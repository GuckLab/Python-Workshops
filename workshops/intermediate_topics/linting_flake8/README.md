# Clean code & Linting

In this workshop we will learn to write clean code following Python's
[PEP8 protocol](https://pep8.org/).

We can "scan" our code for syntax and style problems by **linting**.

One popular linting tool is the
[flake8 package](https://flake8.pycqa.org/en/latest/)
(the "8" comes from the PEP8 name).

## Installing flake8

`pip install flake8`

## Using flake8

`flake8 path/to/file.py`

We can also run it on multiple files or directories:

`flake8 path/to/file.py path/to/directory`

In our case:

`cd workshops/intermediate_topics/linting_flake8`

`flake8 myproj.py`

### Configuring `flake8`

You can easily change the default `flake8` linting behaviour by using a
configuration file. For example, many programmers prefer to have 88 or 120 character
lines rather than the default limit of 80.

You can put these new rules in a `.flake8` file in your project directory.
Take a look at the `.flake8` file in this example.

### Bonus IDE fun!

- You can show a new (or any) line length limit with PyCharm!
    - Go to "Settings > Editor > Code Style" and just give a visual guide e.g. (80, 88)
- You can autoformat your code with PyCharm by hitting "Ctrl+Alt+L"
