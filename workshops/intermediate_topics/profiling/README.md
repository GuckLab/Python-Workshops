# Profiling

Profiling allows us to look at the speed of our code line-by-line.

This is important when we need fast code, want to optimise a program, and
need to remove bottlenecks.

We can use either the built-in `cProfile` or `line_profiler`.
I prefer `line_profiler` because it has microsecond resolution.

## Installation

`pip install line_profiler`

## Using `line_profiler`

- Use the `@profile` decorator on the functions you want to profile.
- Run `kernprof -lv path/to/file.py`

Warning: The `@profile` decorator will cause errors if you run your code normally!
         So it might be a good idea to have a separate `tests/profile_tests folder`.

## Using `cProfile`

cProfile is a built-in Python package with millisecond resolution.
Here is how to use it:

```python
import cProfile
import pstats

def my_func():
    """Some code I have"""
    pass


if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.enable()
    
    # call your code
    my_func()
    
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('tottime')
    stats.print_stats(10)
```