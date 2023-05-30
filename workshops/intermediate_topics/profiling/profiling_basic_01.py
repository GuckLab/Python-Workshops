"""
# Profiling

Profiling allows us to look at the speed of our code line-by-line.

`kernprof -lv workshops/intermediate_topics/profiling/profiling_basic_01.py`

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
