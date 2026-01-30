# functools Utilities Exercises Solutions

from functools import partial

def greet(greeting, name):
    return f"{greeting}, {name}!"

hello = partial(greet, "Hello")
goodbye = partial(greet, "Goodbye")
print(hello("Alice"))  # Hello, Alice!
print(goodbye("Bob"))  # Goodbye, Bob!