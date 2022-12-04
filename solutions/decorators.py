# decorator functions for Advent of Code 2021

def print_debugger(func):
    def new_function(*args, **kwargs):
        print(f"--> Calling {func.__name__} with args={args} and kwargs={kwargs}.")
        return_value = func(*args, **kwargs)
        print(f"--> Result = {return_value}.")
        return return_value

    return new_function
