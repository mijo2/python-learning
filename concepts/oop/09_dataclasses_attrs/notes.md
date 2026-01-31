# Dataclasses & attrs Library Concepts

Brilliant! Composition vs. inheritance taught you flexible design. Now, meet **dataclasses** and **attrs**—tools to eliminate boilerplate in data-focused classes. These auto-generate `__init__`, `__repr__`, `__eq__`, etc., so you focus on logic, not repetition.

Dataclasses are Python's built-in; attrs is a powerful third-party alternative.

## Dataclasses

For classes that are mostly data (fields), use `@dataclass`.

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

person = Person("Alice", 30)
print(person)  # Person(name='Alice', age=30)
```

Auto-generates: `__init__`, `__repr__`, `__eq__`, `__hash__` (if immutable).

### Advanced Features

```python
from dataclasses import dataclass, field

@dataclass
class Employee:
    name: str
    age: int
    salary: float = field(default=50000, repr=False)  # Hide in repr
    skills: list = field(default_factory=list)  # Mutable default

@dataclass(frozen=True)  # Immutable
class Point:
    x: int
    y: int

emp = Employee("Bob", 25)
emp.skills.append("Python")
print(emp)  # Employee(name='Bob', age=25, skills=['Python'])

point = Point(1, 2)
# point.x = 3  # FrozenInstanceError
```

`field()` controls defaults, repr, comparison, etc.

## attrs Library

More powerful than dataclasses: converters, validators, slots.

```python
import attr

@attr.s
class Person:
    name = attr.ib()  # Field
    age = attr.ib()

@attr.s
class Employee(Person):
    salary = attr.ib(default=50000)

# With converters
@attr.s
class Product:
    name = attr.ib()
    price = attr.ib(converter=float)  # Convert to float

emp = Employee("Charlie", 35, 60000)
print(emp)  # Employee(name='Charlie', age=35, salary=60000)
```

Features: auto-slots, validation, inheritance helpers.

## When to Use?

- **Dataclasses**: Simple, built-in, no dependencies.
- **attrs**: Complex validation, conversion, performance.

## Best Practices

- Use for data models, configs, DTOs.
- Combine with protocols/ABCs for behavior.
- Prefer immutable (frozen) for safety.

## Pitfalls

1. **Overuse**: Not for complex logic classes.
2. **Inheritance**: attrs handles it better than dataclasses.
3. **Performance**: attrs uses slots by default.

Create a `Book` dataclass with title, author, pages. Add a method. Compare to manual class. This leads to immutability patterns. You're simplifying code—great job!