# Protocols in Python

## Overview
Protocols define interfaces that classes can implement without explicit inheritance. They enable structural typing, where the shape of an object determines its type rather than its class hierarchy.

## Basic Protocol
```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self, canvas) -> None:
        ...

class Circle:
    def draw(self, canvas) -> None:
        # Implementation
        pass

class Square:
    def draw(self, canvas) -> None:
        # Implementation
        pass

def render_shapes(shapes: list[Drawable]) -> None:
    for shape in shapes:
        shape.draw(canvas)

# Both Circle and Square can be used as Drawable
shapes = [Circle(), Square()]
render_shapes(shapes)
```

## Protocol Methods
```python
from typing import Protocol

class SupportsClose(Protocol):
    def close(self) -> None:
        """Close the resource."""
        ...

class DatabaseConnection:
    def close(self) -> None:
        print("Closing database connection")

class FileHandle:
    def close(self) -> None:
        print("Closing file")

def cleanup_resource(resource: SupportsClose) -> None:
    resource.close()

# Both can be used as SupportsClose
cleanup_resource(DatabaseConnection())
cleanup_resource(FileHandle())
```

## Generic Protocols
```python
from typing import Protocol, TypeVar

T = TypeVar('T')

class Container(Protocol[T]):
    def __getitem__(self, key) -> T:
        ...

    def __setitem__(self, key, value: T) -> None:
        ...

class MyDict(dict):
    pass

def get_first(container: Container[T]) -> T:
    return container[0]

# Usage
d: MyDict[str, int] = MyDict()
get_first(d)  # Type: int
```

## Protocol Inheritance
```python
from typing import Protocol

class Shape(Protocol):
    @property
    def area(self) -> float:
        ...

class DrawableShape(Shape, Protocol):
    def draw(self, canvas) -> None:
        ...

class Circle:
    @property
    def area(self) -> float:
        return 3.14159 * self.radius ** 2

    def draw(self, canvas) -> None:
        # Draw implementation
        pass

# Circle implements both Shape and DrawableShape
def process_shape(shape: DrawableShape) -> None:
    print(f"Area: {shape.area}")
    shape.draw(canvas)
```

## Runtime Checkable Protocols
```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Iterable(Protocol):
    def __iter__(self):
        ...

# Can use isinstance() at runtime
print(isinstance([1, 2, 3], Iterable))  # True
print(isinstance(42, Iterable))        # False
```

## Callback Protocols
```python
from typing import Protocol, Callable

class EventHandler(Protocol):
    def __call__(self, event: str) -> None:
        ...

def register_handler(handler: EventHandler) -> None:
    # Register the handler
    pass

# Functions can be used as EventHandler
def my_handler(event: str) -> None:
    print(f"Handling: {event}")

register_handler(my_handler)

# Callable classes work too
class HandlerClass:
    def __call__(self, event: str) -> None:
        print(f"Class handling: {event}")

register_handler(HandlerClass())
```

## Best Practices
- Use protocols for structural typing
- Name protocols with descriptive suffixes (-able, -er)
- Keep protocols focused on specific behaviors
- Combine protocols with inheritance when appropriate
- Use @runtime_checkable for isinstance checks
