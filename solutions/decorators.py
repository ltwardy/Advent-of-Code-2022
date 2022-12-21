# decorator functions for Advent of Code 2021

import sys


def print_debugger(func):
    def new_function(*args, **kwargs):
        print(f"--> Calling {func.__name__} with args={args} and kwargs={kwargs}.")
        return_value = func(*args, **kwargs)
        print(f"--> Result = {return_value}.")
        return return_value

    return new_function


def conditional_decorator(deco, condition):
    def decorator(func):
        if condition:
            return deco(func)  # decorated
        else:
            return func  # undecorated

    return decorator


def disable_printing(func):
    """Toggle printing for verbosity control."""

    def new_func(*args, **kwargs):
        class DevNull(object):
            def write(self, arg):
                pass

        _stdout = sys.stdout
        sys.stdout = DevNull()

        try:
            return_value = func(*args, **kwargs)
        finally:  # reset stdout in case something goes wrong
            sys.stdout = _stdout
        return return_value

    return new_func
