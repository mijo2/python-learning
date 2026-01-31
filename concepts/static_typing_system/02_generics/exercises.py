"""
02 GENERICS — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise shows what needs to be implemented
- Test your implementations after completion
"""


# Exercise 1: Create generic function
# TODO: Use TypeVar for generic function
def first_element(items):
    """Get first element from any sequence type"""
    from typing import TypeVar
    # TODO: Define TypeVar
    # TODO: Add generic type hints
    pass

# Exercise 2: Create generic class
# TODO: Create class with generic type parameter
class Stack:
    """Generic stack implementation"""
    from typing import TypeVar, Generic
    
    # TODO: Define TypeVar
    # TODO: Make class generic
    # TODO: Implement stack methods with proper types
    pass

# Exercise 3: Constrained generics
# TODO: Limit generic type to specific types
def add_numbers(a, b):
    """Add two numbers of same type"""
    # TODO: Use constrained TypeVar
    # TODO: Ensure type safety
    pass
