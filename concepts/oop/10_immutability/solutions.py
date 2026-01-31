# Immutability Exercises Solutions

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

# Or
from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutablePoint:
    x: int
    y: int