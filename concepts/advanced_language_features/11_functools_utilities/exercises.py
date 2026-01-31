# functools Utilities Exercises

from functools import partial, lru_cache

# Exercise: Use partial to create a greeting function

def greet(greeting, name):
    return f"{greeting}, {name}!"

# TODO: Create hello and goodbye functions
# Uncomment
# hello = partial(greet, "Hello")
# goodbye = partial(greet, "Goodbye")
# print(hello("Alice"))  # Hello, Alice!
# print(goodbye("Bob"))  # Goodbye, Bob!