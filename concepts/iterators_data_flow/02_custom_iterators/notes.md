# Custom Iterators

## Overview
Custom iterators allow you to create objects that can be iterated over using `for` loops or other iteration constructs. They implement the iterator protocol by defining `__iter__` and `__next__` methods.

## Iterator Protocol
- `__iter__()`: Returns the iterator object itself
- `__next__()`: Returns the next item or raises `StopIteration`

## Creating Custom Iterators
```python
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value
```

## Iterator vs Iterable
- **Iterable**: Object with `__iter__` that returns an iterator
- **Iterator**: Object with `__iter__` and `__next__`

## Common Patterns
- **Countdown Iterator**: Counts down from a number
- **Fibonacci Iterator**: Generates Fibonacci sequence
- **File Line Iterator**: Reads lines from a file
- **Infinite Iterator**: Never stops (use with caution)

## Generator Alternative
Generators are often preferred over custom iterators:
```python
def my_generator(data):
    for item in data:
        yield item
```

## Advanced Features
- **Lazy Evaluation**: Compute values only when needed
- **Memory Efficiency**: Don't store entire sequence
- **Infinite Sequences**: Generate values on demand
- **Stateful Iteration**: Maintain iteration state

## Best Practices
- Raise `StopIteration` when exhausted
- Make iterators reusable or single-use as appropriate
- Handle exceptions gracefully
- Document iterator behavior
