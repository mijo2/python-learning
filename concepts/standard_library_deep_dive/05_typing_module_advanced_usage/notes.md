# Advanced Typing Module Usage

## Overview
The `typing` module provides advanced type hints for complex scenarios. These features enable more precise type checking and better IDE support.

## Generic Types
```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

# Usage
int_stack: Stack[int] = Stack()
str_stack: Stack[str] = Stack()
```

## Union Types
```python
from typing import Union

def process_data(data: Union[str, int, float]) -> str:
    if isinstance(data, str):
        return data.upper()
    else:
        return str(data)

# Python 3.10+ union syntax
def process_data(data: str | int | float) -> str:
    return str(data)
```

## Optional Types
```python
from typing import Optional

def find_user(user_id: int) -> Optional[dict]:
    # Return user dict or None
    pass

# Equivalent to Union[dict, None]
```

## Callable Types
```python
from typing import Callable

def apply_function(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)

# Usage
def add(a: int, b: int) -> int:
    return a + b

result = apply_function(add, 1, 2)
```

## Literal Types
```python
from typing import Literal

def set_mode(mode: Literal["read", "write", "append"]) -> None:
    if mode == "read":
        # Read mode logic
        pass
    elif mode == "write":
        # Write mode logic
        pass
    elif mode == "append":
        # Append mode logic
        pass
```

## TypedDict
```python
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str

def create_person(name: str, age: int, email: str) -> Person:
    return {"name": name, "age": age, "email": email}
```

## Protocol Classes
```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self, canvas) -> None:
        ...

def render_objects(objects: list[Drawable]) -> None:
    for obj in objects:
        obj.draw(canvas)
```

## NewType
```python
from typing import NewType

UserId = NewType('UserId', int)
ProductId = NewType('ProductId', int)

def get_user(user_id: UserId) -> dict:
    # user_id is guaranteed to be a UserId
    pass

# Prevent mixing different ID types
user_id = UserId(123)
product_id = ProductId(456)

# This would be a type error
get_user(product_id)  # Error!
```

## Best Practices
- Use specific types over generic ones when possible
- Leverage Literal for enumerated values
- Use Protocol for structural typing
- Create domain-specific types with NewType
- Keep type hints readable and maintainable
