"""
# Profiling

Profiling allows us to look at the speed of our code line-by-line.

This is important when we need fast code, want to optimise a program, and
need to remove bottlenecks.

We can use either the built-in `cProfile` or `line_profiler`.
I prefer `line_profiler` because it has microsecond resolution.

## Installation

`pip install line_profiler`

## Using `line_profiler`

- Place the `@profile` decorator on the functions you want to profile.
- Run `kernprof -lv path/to/file.py` e.g. `kernprof -lv workshops/intermediate_topics/profiling.py`

Warning: The `@profile` decorator will cause errors if you run your code normally!
"""

import numpy as np

arr = np.array([2, 5, 6, 8, 7, 5, 7, 8])
listy = arr.tolist()


@profile
def func_np_shorthand(a):
    a += 5

@profile
def func_np(a):
    a = a + 5


@profile
def func_list_comp(a):
    a_add = [i + 5 for i in a]


@profile
def func_loop(a):
    a_add = []
    for i in a:
        a_add.append(i + 5)


if __name__ == '__main__':
    func_np(a=arr)
    func_np_shorthand(a=arr)
    func_list_comp(a=listy)
    func_loop(a=listy)
