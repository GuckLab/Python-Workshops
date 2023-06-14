"""
# Profiling

Profiling allows us to look at the speed of our code line-by-line.

kernprof -lv workshops/intermediate_topics/loops_other/profiling_loops.py

"""


@profile
def use_for_loop(iterable):
    output = []
    for i in iterable: output.append(i ** 2)
    return list(output)


@profile
def use_list_comprehension(iterable):
    output = [i ** 2 for i in iterable]
    return list(output)


@profile
def use_generator_expression(iterable):
    output = (i ** 2 for i in iterable)
    return list(output)


if __name__ == '__main__':
    # create a generator and list
    my_generator = (i for i in range(10000))
    my_lst = [i ** 2 for i in my_generator]

    test = "range"

    if test == 'list':
        use_for_loop(my_lst)
        use_list_comprehension(my_lst)
        use_generator_expression(my_lst)
    elif test == 'gen':
        use_for_loop(my_generator)
        use_list_comprehension(my_generator)
        use_generator_expression(my_generator)
    elif test == 'range':
        use_for_loop(range(10000))
        use_list_comprehension(range(10000))
        use_generator_expression(range(10000))
    else:
        raise ValueError("Allowed values are: list, gen, range")