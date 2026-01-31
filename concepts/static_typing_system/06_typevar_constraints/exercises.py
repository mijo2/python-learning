"""
06 TYPEVAR CONSTRAINTS — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise shows what needs to be implemented
- Test your implementations after completion
"""


# Exercise 1: Basic constrained TypeVar
# TODO: Create TypeVar limited to specific types
from typing import TypeVar

# TODO: Create constrained TypeVar for numbers
NumericType = TypeVar('NumericType', int, float)

def add_numbers(a: NumericType, b: NumericType) -> NumericType:
    """Add two numbers of same type"""
    return a + b

# Exercise 2: Bound TypeVar
# TODO: Create TypeVar bound to a base class
from typing import TypeVar

# TODO: Create TypeVar bound to str
StringLike = TypeVar('StringLike', bound=str)

def get_length(s: StringLike) -> int:
    """Get length of string-like object"""
    return len(s)

# Exercise 3: Complex constraints
# TODO: Use constraints with protocols
from typing import Protocol

class HasLength(Protocol):
    def __len__(self) -> int: ...

LengthyType = TypeVar('LengthyType', bound=HasLength)

def get_length_generic(item: LengthyType) -> int:
    """Get length of any object with __len__"""
    return len(item)
