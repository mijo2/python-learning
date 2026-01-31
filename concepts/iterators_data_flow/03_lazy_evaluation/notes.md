# Lazy Evaluation

## Overview
Lazy evaluation is a strategy where expressions are not evaluated until their values are actually needed. This can improve performance by avoiding unnecessary computations and reducing memory usage.

## Key Concepts
- **Eager Evaluation**: Compute values immediately
- **Lazy Evaluation**: Defer computation until needed
- **Short-circuiting**: Stop evaluation when result is determined

## Python Lazy Features
- **Generators**: `yield` creates lazy iterators
- **Generator Expressions**: `(x for x in iterable if condition)`
- **Iterator Protocol**: `__next__` computes on demand
- **Short-circuit Operators**: `and`, `or`, `if-else`

## Benefits
- **Memory Efficiency**: Don't store entire collections
- **Performance**: Avoid unnecessary computations
- **Infinite Sequences**: Handle infinite data streams
- **Composability**: Chain operations without intermediate storage

## Examples
```python
# Lazy filtering
def lazy_filter(func, iterable):
    for item in iterable:
        if func(item):
            yield item

# Short-circuit evaluation
result = expensive_operation() or default_value
```

## Lazy vs Eager
```python
# Eager: computes all
squares = [x**2 for x in range(1000000)]

# Lazy: computes on demand
squares = (x**2 for x in range(1000000))
```

## Common Patterns
- **Lazy Lists**: Compute elements when accessed
- **Lazy Properties**: Compute attributes on first access
- **Lazy Loading**: Load data when first requested
- **Infinite Generators**: Generate values indefinitely

## Considerations
- **Debugging**: Harder to debug lazy computations
- **Exceptions**: May occur later than expected
- **Resource Management**: Ensure cleanup happens
- **Performance Trade-offs**: Setup cost vs computation cost
