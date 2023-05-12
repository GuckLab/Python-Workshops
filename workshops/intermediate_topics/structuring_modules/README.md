## What is a Python Module and Python Package.

## How should I lay out my modules?

General overview:

- my_repo
   - **my_project**
      - __init__.py
      - cli.py
      - folder1
        - __init__.py
        - code_in_folder1.py
      - folder2
        - __init__.py
        - code_in_folder2.py
   - **tests**
      - test_cli.py 
      - test_code_in_folder1.py 
      - test_code_in_folder2.py 
      - requirements.txt
   - docs
      - index.rst
      - requirements.txt
   - setup.py (or pyproject.toml)
   - README.md
   - .gitignore
   - etc. (gitlabci.yml, LICENSE)
 

With this layout, you can install your package with pip. This will allow
you to run your tests via the terminal!

## Where do I put my classes and functions?

## What about my scripts or CLI?

## Individual Files
In Python there are several files that can be used to install your package.
The most common one is `setup.py`. The current standard is `pyproject.toml`.

### setup.py overview
We will first talk about `setup.py`. See an example in this directory!

The `setup.py` is a python file! So you can add functions and functionality to it.
  - This also means that it has limitations when it comes to building other tools,
    like C/C++ dependencies.


In general, this file should contain:
- The **name** of the package
- The **maintainer**(s) of the package
- The **version** of the package
- Where the package is stored (github/gitlab **url** etc.)
- What are the **dependencies** (`install_requires`) of the package i.e. what needs to be installed
  before your package will run. The dependencies are the other
  packages that your package relies upon, and will be installed by `pip` or
  `conda` before your package is installed.
  - These can include packages/libraries on pypi.org (e.g. numpy, pandas),
    git repositories (public or private), local packages and more.
  - C .dll files and other non-standard file can also be included! 
- **Python version**(s) with which the package is compatible 
- It should also link-to/mention the **License**, and some **meta info**.


### setup.py detailed description

Here is a description of some of the more complicated parts of the
`setup` function from the accompanying `setup.py` file.


  - ```python
    package_dir={name: name}
    ```
    `name` here the name of your package. In the
    general overview above, this would be `"my_project"`.
    For dclab, it would be `"dclab"`

  - ```python
    packages=find_packages()
    ```
    this will automatically find all modules in your
    package_dir` that are valid Python modules i.e. they contain an `__init__.py` file.

  - ```python
    install_requires=[
        "h5py>=3.0.0",
        "numpy>=1.17.0",
        # private git repo
        # you can use tags (@0.1.23), branches (@my_branch) and commits (@commit_hash) instead of @main here
        "private_repo_example@git+ssh://git@gitlab.example_gitlab.com/group_name/private_repo_example.git@main",
    ],
    ```
    `install_requires` is a list of the dependencies in string format. If you
    are used to using a requirements.txt file, then this will look familiar!
    Notice how you can include a git repo (private or public) with ssh (or https).
    In general, you should set minimum versions of the packages, as old versions
    might not work with newer code or python versions.

  - ```python
    python_requires=">=3.8",
    ```
    Here you can define the Python version(s) with which your package works.
    In general, you should set a minimum version (3.8 is usually okay).

  - ```python
    include_package_data=True,
    package_data={"my_project": [
        # dll
        'devices/pressure_sensors/SensorCompany/libs/64bit/*.dll',
        # requirements files
        'some/random/other/file/requirements.txt',
    ]},
    ```
    `package_data` here is a dictionary of `{package: [file1.dll, file2.txt]}`.
    These files are not included by default by the `find_packages` function from above,
    and therefore must be included manually here!
    If you are using non-standard `package_data`, such as the above .dll example files,
    then you should set `include_package_data=True`.