# Immutability Exercises

# Exercise: Immutability Patterns
# Create an immutable class using frozen dataclass or namedtuple.

# TODO: Implement immutable Point
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

# Or using dataclass
from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutablePoint:
    pass