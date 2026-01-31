# Immutability Patterns

Awesome! Dataclasses and attrs simplified data classes. Now, embrace **immutability**—objects that can't be changed after creation. This prevents bugs from accidental mutations and aids concurrency. Python has tools like namedtuples and frozen dataclasses.

Immutable objects are "write once, read many."

## Why Immutability?

1. **Safety**: No side effects from changes.
2. **Thread-Safe**: No race conditions in multi-threading.
3. **Hashable**: Use as dict keys or set elements.
4. **Functional Style**: Encourages pure functions.

## Namedtuples

Lightweight, immutable structs.

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)  # 1
# p.x = 3  # AttributeError
print(p)    # Point(x=1, y=2)
```

- Factory function creates class.
- Accessible by index or name.
- Immutable, hashable, lightweight.

## Frozen Dataclasses

Immutable dataclasses.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutablePerson:
    name: str
    age: int

person = ImmutablePerson("David", 40)
# person.age = 41  # FrozenInstanceError
print(person)  # ImmutablePerson(name='David', age=40)
```

- All fields immutable.
- Auto `__eq__`, `__hash__`.

## Other Patterns

1. **Tuples**: Simple immutability.
   ```python
   point = (1, 2)
   ```

2. **Frozensets**: Immutable sets.
   ```python
   fs = frozenset([1, 2, 3])
   ```

3. **Strings/Ints**: Already immutable.

## Implementing Custom Immutability

For classes, override `__setattr__` to prevent changes.

```python
class Immutable:
    def __init__(self, value):
        self._value = value
    
    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError("Immutable")
        super().__setattr__(name, value)
    
    @property
    def value(self):
        return self._value
```

## Best Practices

- Use immutability for configs, constants, shared data.
- Combine with functional programming.
- For mutable needs, return new instances.

## Pitfalls

1. **Performance**: Creating many copies can be costly—use carefully.
2. **Nested Mutability**: Immutable container with mutable contents—deep copy if needed.
3. **Over-Immutability**: Not everything needs it—balance with practicality.

Create an immutable `Vector` using namedtuple or frozen dataclass. Compare to mutable version. This ties into slots for optimization. You're mastering data integrity—excellent!