# Function Decorators Exercises

from functools import wraps

# Exercise: Create a logging decorator

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# TODO: Apply @logger to a function
# Uncomment
# @logger
# def add(a, b):
#     return a + b

# add(1, 2)