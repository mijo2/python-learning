# Generics in Python

## Overview
Generics allow you to write reusable code that works with different types while maintaining type safety. Python's typing system supports generics through TypeVar and Generic base classes.

## TypeVar
```python
from typing import TypeVar

T = TypeVar('T')  # Can be any type
U = TypeVar('U')

def swap(a: T, b: T) -> tuple[T, T]:
    return b, a

# Usage
x, y = swap(1, 2)        # T is int
a, b = swap("a", "b")    # T is str
```

## Generic Classes
```python
from typing import Generic, TypeVar

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def is_empty(self) -> bool:
        return len(self.items) == 0

# Usage
int_stack: Stack[int] = Stack()
str_stack: Stack[str] = Stack()
```

## Constrained TypeVar
```python
from typing import TypeVar

# T must be int or float
NumberT = TypeVar('NumberT', int, float)

def add(x: NumberT, y: NumberT) -> NumberT:
    return x + y

# Valid
result1 = add(1, 2)        # NumberT is int
result2 = add(1.0, 2.0)    # NumberT is float

# Invalid (would be type error)
# result3 = add("a", "b")  # str is not allowed
```

## Generic Functions
```python
from typing import TypeVar, Sequence

T = TypeVar('T')

def first_item(items: Sequence[T]) -> T:
    return items[0]

def reverse(items: Sequence[T]) -> list[T]:
    return list(reversed(items))

# Usage
numbers = [1, 2, 3, 4]
first = first_item(numbers)  # Type: int
reversed_nums = reverse(numbers)  # Type: list[int]
```

## Multiple TypeVars
```python
from typing import TypeVar

T = TypeVar('T')
U = TypeVar('U')

def combine(a: T, b: U) -> tuple[T, U]:
    return a, b

# Usage
result = combine(1, "hello")  # tuple[int, str]
```

## Generic Methods
```python
from typing import Generic, TypeVar

T = TypeVar('T')
U = TypeVar('U')

class Converter(Generic[T, U]):
    def convert(self, value: T) -> U:
        # Implementation would depend on T and U
        pass

# Usage
str_converter: Converter[str, int] = Converter()
```

## Best Practices
- Use meaningful TypeVar names
- Constrain TypeVars when appropriate
- Use Generic base class for generic classes
- Leverage generics for reusable, type-safe code
- Combine with protocols for structural typing
