"""
01 CLOSURES — EXERCISES

Instructions:
- Learn about closures and variable capture in nested functions
- Implement functions that create and return closures
- Understand how closures preserve their environment
"""

# Exercise 1: Create a simple closure
# TODO: Create a function that returns a closure for multiplication
def make_multiplier(factor):
    """
    Return a function that multiplies its argument by factor.
    This demonstrates how closures capture variables from their defining scope.
    """
    # TODO: Define an inner function that multiplies its parameter by factor
    # TODO: Return the inner function
    pass

# Exercise 2: Closure with multiple captured variables
# TODO: Create a closure that captures multiple variables
def make_power_function(base, exponent):
    """
    Return a function that raises base to the power of exponent.
    Demonstrates capturing multiple variables in a closure.
    """
    # TODO: Define inner function that computes base ** exponent
    # TODO: Return the inner function (no parameters needed)
    pass

# Exercise 3: Closure for counting
# TODO: Create a closure that maintains state between calls
def make_counter():
    """
    Return a function that returns an incrementing counter value.
    Shows how closures can maintain state without global variables.
    """
    # TODO: Initialize a counter variable in the outer function
    # TODO: Define inner function that increments and returns counter
    # TODO: Return the inner function
    pass

# Exercise 4: Closure with lists and mutation
# TODO: Create a closure that works with mutable objects
def make_list_appender():
    """
    Return a function that appends items to an internal list and returns the list.
    Demonstrates how closures work with mutable objects.
    """
    # TODO: Initialize an empty list in the outer function
    # TODO: Define inner function that appends item to the list
    # TODO: Return the current state of the list
    # TODO: Return the inner function
    pass

# Exercise 5: Multiple closures sharing state
# TODO: Create multiple closures that share the same captured variables
def make_shared_counter():
    """
    Return two functions that share the same counter.
    Shows how multiple closures can share the same environment.
    """
    # TODO: Initialize shared counter variable
    # TODO: Define increment function
    # TODO: Define decrement function
    # TODO: Return both functions as a tuple
    pass

# Test code (uncomment after implementation)
# if __name__ == "__main__":
#     # Test make_multiplier
#     double = make_multiplier(2)
#     triple = make_multiplier(3)
#     print(f"double(5) = {double(5)}")  # Should be 10
#     print(f"triple(5) = {triple(5)}")  # Should be 15
#
#     # Test make_power_function
#     square = make_power_function(2, 2)  # base=2, exponent=2
#     cube = make_power_function(3, 3)    # base=3, exponent=3
#     print(f"square() = {square()}")     # Should be 4 (2^2)
#     print(f"cube() = {cube()}")         # Should be 27 (3^3)
#
#     # Test make_counter
#     counter = make_counter()
#     print(f"counter() = {counter()}")   # Should be 1
#     print(f"counter() = {counter()}")   # Should be 2
#     print(f"counter() = {counter()}")   # Should be 3
#
#     # Test make_list_appender
#     appender = make_list_appender()
#     print(f"appender('a') = {appender('a')}")  # Should be ['a']
#     print(f"appender('b') = {appender('b')}")  # Should be ['a', 'b']
#     print(f"appender('c') = {appender('c')}")  # Should be ['a', 'b', 'c']
#
#     # Test make_shared_counter
#     increment, decrement = make_shared_counter()
#     print(f"increment() = {increment()}")     # Should be 1
#     print(f"increment() = {increment()}")     # Should be 2
#     print(f"decrement() = {decrement()}")     # Should be 1
#     print(f"increment() = {increment()}")     # Should be 2
