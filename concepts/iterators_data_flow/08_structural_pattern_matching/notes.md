# Structural Pattern Matching

## Overview
Structural pattern matching, introduced in Python 3.10 with the `match` statement, allows for powerful and expressive conditional execution based on the structure of data. It's similar to switch statements but much more flexible.

## Basic Syntax
```python
match value:
    case pattern1:
        # code
    case pattern2:
        # code
    case _:
        # default
```

## Pattern Types
- **Literal Patterns**: Match exact values (`case 1:`)
- **Variable Patterns**: Capture values (`case x:`)
- **Wildcard Patterns**: Match anything (`case _:`)
- **OR Patterns**: Multiple patterns (`case 1 | 2:`)
- **Sequence Patterns**: Match sequences (`case [x, y]:`)
- **Mapping Patterns**: Match dictionaries (`case {"key": value}:`)
- **Class Patterns**: Match object attributes (`case Point(x, y):`)

## Sequence Patterns
```python
data = [1, 2, 3, 4]

match data:
    case [x]:  # Single element
        print(f"One element: {x}")
    case [x, y]:  # Two elements
        print(f"Two elements: {x}, {y}")
    case [x, y, *rest]:  # Head and tail
        print(f"First: {x}, second: {y}, rest: {rest}")
    case _:  # Anything else
        print("Other")
```

## Mapping Patterns
```python
config = {"host": "localhost", "port": 8080}

match config:
    case {"host": host, "port": 80, **rest}:
        print(f"HTTP: {host}, extra: {rest}")
    case {"host": host, "port": port}:
        print(f"Other: {host}:{port}")
```

## Class Patterns
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(1, 2)

match point:
    case Point(x=0, y=0):
        print("Origin")
    case Point(x=x, y=y):
        print(f"Point: {x}, {y}")
```

## Guards
Add conditions to patterns:
```python
match value:
    case x if x > 0:
        print("Positive")
    case x if x < 0:
        print("Negative")
    case 0:
        print("Zero")
```

## Advanced Features
- **Nested Patterns**: Patterns within patterns
- **AS Patterns**: `case Point(x, y) as p:`
- **Pattern Matching in Loops**: `for case in data:`
- **Type Matching**: Match based on types

## Best Practices
- Use for complex conditional logic
- Prefer over long if-elif chains
- Keep patterns readable
- Use guards for additional conditions
- Consider performance vs readability
