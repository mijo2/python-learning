# TypeVar Constraints in Python

## Overview
TypeVar constraints limit the possible types that can be substituted for a type variable. This provides more precise type checking while maintaining flexibility.

## Basic Constraints
```python
from typing import TypeVar

# T can only be int or str
ConstrainedT = TypeVar('ConstrainedT', int, str)

def process_value(value: ConstrainedT) -> ConstrainedT:
    if isinstance(value, int):
        return value * 2
    elif isinstance(value, str):
        return value.upper()
    return value  # This won't execute due to type constraints

# Valid usage
result1 = process_value(42)      # ConstrainedT is int
result2 = process_value("hello") # ConstrainedT is str

# Invalid (type error)
# result3 = process_value([1, 2, 3])  # list not allowed
```

## Union vs Constrained TypeVar
```python
from typing import TypeVar, Union

# These are equivalent
ConstrainedT = TypeVar('ConstrainedT', int, str, float)
UnionT = Union[int, str, float]

def func1(x: ConstrainedT) -> ConstrainedT:
    return x

def func2(x: UnionT) -> UnionT:
    return x

# But TypeVar preserves the specific type
num: int = 5
result1 = func1(num)  # Type: int
result2 = func2(num)  # Type: Union[int, str, float]
```

## Constraints with Generic Classes
```python
from typing import TypeVar, Generic

SerializableT = TypeVar('SerializableT', int, str, dict)

class Serializer(Generic[SerializableT]):
    def serialize(self, data: SerializableT) -> str:
        if isinstance(data, dict):
            return json.dumps(data)
        return str(data)

    def deserialize(self, data: str) -> SerializableT:
        # Type checker knows return type matches input type
        pass

# Usage
int_serializer = Serializer[int]()
str_serializer = Serializer[str]()
```

## Bound TypeVar
```python
from typing import TypeVar

# T must be a subclass of str
StrSubclass = TypeVar('StrSubclass', bound=str)

def process_string(s: StrSubclass) -> StrSubclass:
    return s.upper()

class MyString(str):
    pass

# Valid
result = process_string(MyString("hello"))

# Invalid (type error)
# result = process_string(123)  # int is not a str subclass
```

## Complex Constraints
```python
from typing import TypeVar, Protocol

class HasLength(Protocol):
    def __len__(self) -> int:
        ...

# T must implement HasLength protocol
LengthyT = TypeVar('LengthyT', bound=HasLength)

def get_length(item: LengthyT) -> int:
    return len(item)

# Valid for any type with __len__
get_length("string")
get_length([1, 2, 3])
get_length({"a": 1, "b": 2})
```

## Multiple Constraints
```python
from typing import TypeVar

# T must be one of these specific types
AllowedTypes = TypeVar('AllowedTypes', int, float, complex)

def math_operation(x: AllowedTypes, y: AllowedTypes) -> AllowedTypes:
    return x + y

# All combinations are type-safe
result1 = math_operation(1, 2)        # int
result2 = math_operation(1.0, 2.0)    # float
result3 = math_operation(1+2j, 3+4j)  # complex
```

## Best Practices
- Use constraints to limit acceptable types
- Prefer bound constraints for inheritance relationships
- Use union constraints for specific allowed types
- Keep constraints as specific as needed but not overly restrictive
- Combine with protocols for structural constraints
