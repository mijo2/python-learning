# TypedDict in Python

## Overview
TypedDict allows you to define dictionaries with specific key-value type contracts. It provides type safety for dictionary-based data structures while maintaining runtime compatibility.

## Basic TypedDict
```python
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str

# Usage
person: Person = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com"
}

# Type checker will catch errors
# person["age"] = "thirty"  # Type error!
```

## Required vs Optional Keys
```python
from typing import TypedDict, NotRequired, Required

class Person(TypedDict, total=False):
    name: str           # Required (overridden by total=False)
    age: int            # Required
    email: NotRequired[str]  # Optional

# Or using Required
class StrictPerson(TypedDict):
    name: Required[str]
    age: Required[int]
    email: NotRequired[str]
```

## Nested TypedDict
```python
from typing import TypedDict

class Address(TypedDict):
    street: str
    city: str
    zip_code: str

class Person(TypedDict):
    name: str
    age: int
    address: Address

person: Person = {
    "name": "Bob",
    "age": 25,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "zip_code": "12345"
    }
}
```

## Alternative Syntax (Python 3.6.1+)
```python
from typing import TypedDict

# Equivalent to class syntax
Person = TypedDict('Person', {
    'name': str,
    'age': int,
    'email': str
})
```

## Inheritance
```python
class BasePerson(TypedDict):
    name: str
    age: int

class Employee(BasePerson):
    employee_id: int
    department: str

employee: Employee = {
    "name": "Charlie",
    "age": 35,
    "employee_id": 12345,
    "department": "Engineering"
}
```

## Generic TypedDict
```python
from typing import TypedDict, TypeVar, Generic

T = TypeVar('T')

class Response(TypedDict, Generic[T]):
    status: str
    data: T

# Usage
user_response: Response[dict] = {
    "status": "success",
    "data": {"name": "Alice", "id": 1}
}
```

## Runtime Usage
```python
# TypedDict is compatible with regular dict operations
person = Person(name="Alice", age=30, email="alice@example.com")

# Can be used like regular dict
print(person["name"])
person["age"] = 31

# isinstance check (if using @runtime_checkable protocols)
from typing import runtime_checkable

@runtime_checkable
class Person(TypedDict, Protocol):
    name: str
    age: int

print(isinstance(person, Person))  # True
```

## Best Practices
- Use TypedDict for structured dictionary data
- Prefer classes for complex objects with methods
- Use NotRequired for optional fields
- Keep TypedDict definitions simple and focused
- Combine with dataclasses for more complex scenarios
