"""
03 FUNCTION DECORATORS — EXERCISES

Instructions:
- Learn about function decorators and how they modify function behavior
- Implement decorators that add functionality to existing functions
- Understand decorator syntax and best practices
"""

# Exercise 1: Create a simple logging decorator
# TODO: Create a decorator that logs when a function is called and what it returns
def logging_decorator(func):
    """
    Decorator that logs function calls and return values.
    Use functools.wraps to preserve function metadata.
    """
    from functools import wraps

    # TODO: Use @wraps(func) decorator
    # TODO: Define wrapper function
    # TODO: Print "Calling {function_name} with args: {args}, kwargs: {kwargs}"
    # TODO: Call the original function and store result
    # TODO: Print "{function_name} returned: {result}"
    # TODO: Return the result
    pass

# Exercise 2: Create a timing decorator
# TODO: Create a decorator that measures and prints function execution time
def timing_decorator(func):
    """
    Decorator that measures function execution time.
    """
    from functools import wraps
    import time

    # TODO: Use @wraps(func) decorator
    # TODO: Record start time
    # TODO: Call original function
    # TODO: Record end time
    # TODO: Calculate duration
    # TODO: Print execution time
    # TODO: Return result
    pass

# Exercise 3: Create a decorator that caches results
# TODO: Implement a simple memoization decorator
def memoize_decorator(func):
    """
    Decorator that caches function results to avoid recomputation.
    Use function arguments as cache keys.
    """
    from functools import wraps

    # TODO: Initialize cache dictionary in outer scope
    # TODO: Use @wraps(func)
    # TODO: Create cache key from args and kwargs
    # TODO: Check if result is cached
    # TODO: If not cached, compute and cache result
    # TODO: Return cached result
    pass

# Exercise 4: Decorator with parameters
# TODO: Create a decorator that accepts its own parameters
def repeat_decorator(times):
    """
    Decorator that repeats function execution multiple times.
    Returns a list of all return values.
    """
    def decorator(func):
        from functools import wraps

        # TODO: Use @wraps(func)
        # TODO: Execute func 'times' number of times
        # TODO: Collect all results in a list
        # TODO: Return the list of results
        pass
    return decorator

# Exercise 5: Stacking decorators
# TODO: Apply multiple decorators to a single function
@logging_decorator  # TODO: Uncomment when logging_decorator is implemented
@timing_decorator   # TODO: Uncomment when timing_decorator is implemented
def complex_function(x, y, delay=0.1):
    """
    A function that does some computation with a delay.
    Used to demonstrate decorator stacking.
    """
    import time
    time.sleep(delay)
    return x ** y

# Exercise 6: Class-based decorator
# TODO: Create a decorator using a class instead of a function
class CountCalls:
    """
    Class-based decorator that counts how many times a function is called.
    """

    def __init__(self, func):
        # TODO: Store the function
        # TODO: Initialize call count
        pass

    def __call__(self, *args, **kwargs):
        # TODO: Increment call count
        # TODO: Call the original function
        # TODO: Print call count
        # TODO: Return result
        pass

# Test code (uncomment after implementation)
# if __name__ == "__main__":
#     print("=== Function Decorators Demo ===\n")
#
#     # Test logging decorator
#     print("1. Logging Decorator:")
#     @logging_decorator
#     def add(a, b):
#         return a + b
#
#     result = add(3, 5)
#     print(f"Result: {result}\n")
#
#     # Test timing decorator
#     print("2. Timing Decorator:")
#     @timing_decorator
#     def slow_function():
#         import time
#         time.sleep(0.5)
#         return "Done"
#
#     result = slow_function()
#     print(f"Result: {result}\n")
#
#     # Test memoization decorator
#     print("3. Memoization Decorator:")
#     @memoize_decorator
#     def fibonacci(n):
#         if n < 2:
#             return n
#         return fibonacci(n-1) + fibonacci(n-2)
#
#     print(f"fibonacci(10) = {fibonacci(10)}")  # Should be fast on second call
#     print(f"fibonacci(10) = {fibonacci(10)}")  # Should use cache
#     print()
#
#     # Test parameterized decorator
#     print("4. Parameterized Decorator:")
#     @repeat_decorator(3)
#     def random_number():
#         import random
#         return random.randint(1, 10)
#
#     results = random_number()
#     print(f"Random numbers: {results}")
#     print()
#
#     # Test stacked decorators
#     print("5. Stacked Decorators:")
#     result = complex_function(2, 3, delay=0.2)
#     print(f"complex_function result: {result}")
#     print()
#
#     # Test class-based decorator
#     print("6. Class-Based Decorator:")
#     @CountCalls
#     def greet(name):
#         return f"Hello, {name}!"
#
#     greet("Alice")
#     greet("Bob")
#     greet("Charlie")
