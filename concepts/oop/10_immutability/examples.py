# Immutability Patterns Examples

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
# p.x = 3  # AttributeError: can't set attribute

from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutablePerson:
    name: str
    age: int

person = ImmutablePerson("David", 40)
# person.age = 41  # FrozenInstanceError