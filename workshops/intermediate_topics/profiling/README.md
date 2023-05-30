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
