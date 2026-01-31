# Object Interning in Python

## Overview
Object interning is an optimization technique where Python reuses immutable objects instead of creating new ones. This saves memory and can speed up comparisons.

## When Does Interning Happen?
- Small integers (-5 to 256)
- Short strings (identifiers, literals)
- Some other cases

## Key Points
- `is` checks identity (same object)
- `==` checks equality (same value)
- Interned objects are singletons for their value

## Examples
```python
a = 256
b = 256
print(a is b)  # True (interned)

x = 257
y = 257
print(x is y)  # False (not interned)

s1 = "hello"
s2 = "hello"
print(s1 is s2)  # True (interned)

s3 = "hello world"
s4 = "hello world"
print(s3 is s4)  # False (not interned, has space)
```

## Manual Interning
- Use `sys.intern()` for strings
- Useful for dictionaries with many repeated string keys

## Gotchas
- Don't rely on interning for logic, use == for comparisons
- Interning behavior can vary between Python versions