"""
05 PARAMSPEC — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise shows what needs to be implemented
- Test your implementations after completion
"""


# Exercise 1: Basic ParamSpec usage
# TODO: Create generic decorator with ParamSpec
from typing import TypeVar, Callable, ParamSpec

P = ParamSpec('P')
T = TypeVar('T')

def logging_decorator(func: Callable[P, T]) -> Callable[P, T]:
    """Generic logging decorator"""
    # TODO: Preserve original function signature
    # TODO: Add logging functionality
    # TODO: Return result
    pass

# Exercise 2: Decorator with complex signature
# TODO: Decorate function with multiple parameters
@logging_decorator
def complex_function(a: int, b: str, c: float = 1.0) -> str:
    """Function with complex signature"""
    return f"{a}, {b}, {c}"

# Exercise 3: Async function decorator
# TODO: Create decorator for async functions
async def async_logging_decorator(func: Callable[P, Awaitable[T]]) -> Callable[P, Awaitable[T]]:
    """Decorator for async functions"""
    # TODO: Handle async function signatures
    # TODO: Add async logging
    pass
