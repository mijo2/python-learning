# Iterator Protocol

Dive into iterators! The iterator protocol allows objects to be looped over, powering `for` loops and more. It's the backbone of Python's iteration.

## What is the Iterator Protocol?

Objects implementing `__iter__` (returning an iterator) and `__next__` (yielding values) follow this protocol.

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

for item in MyIterator([1, 2, 3]):
    print(item)  # 1, 2, 3
```

## Key Components

- **Iterable**: Has `__iter__`, returns iterator.
- **Iterator**: Has `__next__`, raises `StopIteration` when done.

## Why It Matters

- **Memory Efficiency**: Generate values on demand.
- **Flexibility**: Custom iteration logic.
- **Integration**: Works with built-ins like `list()`, `sum()`.

Experiment with custom iterators for sequences or infinite streams!