# Mutability Rules in Python

## Overview
Python objects can be mutable or immutable. Understanding mutability is crucial for avoiding bugs related to shared references and unexpected modifications.

## Immutable Types
- `int`, `float`, `str`, `tuple`, `frozenset`, `bytes`
- Once created, their value cannot be changed
- Operations create new objects

## Mutable Types
- `list`, `dict`, `set`, `bytearray`
- Can be modified in-place

## Key Concepts
- Shared references: Multiple variables pointing to the same object
- Aliasing: When two variables refer to the same mutable object
- Copying: Shallow vs deep copy

## Common Pitfalls
- Modifying a list while iterating
- Default mutable arguments in functions
- Unintended sharing of mutable objects

## Examples
```python
# Immutable
x = 5
y = x
x += 1  # Creates new int object
print(y)  # Still 5

# Mutable
lst1 = [1, 2, 3]
lst2 = lst1
lst1.append(4)
print(lst2)  # [1, 2, 3, 4] - modified!
```