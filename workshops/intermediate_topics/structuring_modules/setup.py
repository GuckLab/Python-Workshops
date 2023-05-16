#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import exists, dirname, realpath
from setuptools import setup, find_packages
import sys


maintainer = "Eoghan O'Connell"
maintainer_email = "eoghan.oconnell@mpl.mpg.de"
description = "My repo for such and such project"
name = "my_project"
year = "2023"

sys.path.insert(0, realpath(dirname(__file__)) + "/" + name)


setup(
    name=name,
    maintainer=maintainer,
    maintainer_email=maintainer_email,
    url="https://awesome_project.org",
    version="0.0.1",
    license="Custom - See LICENSE file",
    description=description,
    long_description=open("README.md").read() if exists("README.md") else "",

    install_requires=[
        "h5py>=3.0.0",
        "numpy>=1.17.0",
        # private git repo
        # you can use tags (@0.1.23), branches (@my_branch) and commits (@commit_hash) instead of @main here
        "private_repo_example@git+ssh://git@gitlab.example_gitlab.com/group_name/private_repo_example.git@main",
    ],
    python_requires=">=3.8",

    package_dir={name: name},
    packages=find_packages(),
    include_package_data=True,
    package_data={"my_project": [
        # dll
        'devices/pressure_sensors/SensorCompany/libs/64bit/*.dll',
        # requirements files
        'some/random/other/file/requirements.txt',
    ]},

    keywords=["SCIENCE", "wow", "5 stars"],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Private",
    ],
    platforms=["ALL"],
)
