# Memory Efficient Iteration

## Overview
Memory efficient iteration focuses on processing data without loading entire collections into memory. This is crucial when working with large datasets, files, or infinite sequences.

## Core Principles
- **Lazy Evaluation**: Compute values on demand
- **Streaming**: Process data in chunks
- **Generators**: Yield values instead of storing
- **Iterators**: Traverse without storing entire collection

## Memory Comparison
```python
# Inefficient: loads all into memory
data = list(range(1000000))
processed = [x * 2 for x in data]

# Efficient: processes on demand
data = range(1000000)
processed = (x * 2 for x in data)
```

## Techniques
- **Generator Expressions**: `(expr for item in iterable)`
- **Generator Functions**: `def gen(): yield value`
- **Itertools**: `islice`, `takewhile`, `dropwhile`
- **File Iteration**: `for line in file:`

## Large File Processing
```python
# Memory efficient file reading
def process_large_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            process_line(line.strip())
```

## Infinite Sequences
```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Use with caution
for num in fibonacci():
    if num > 1000:
        break
    print(num)
```

## Memory Profiling
- Use `sys.getsizeof()` to check object sizes
- Monitor memory usage with `psutil` or `memory_profiler`
- Profile with `cProfile` and `memory_profiler`

## Common Pitfalls
- **Accidental Eager Evaluation**: `list(generator)`
- **Holding References**: Keeping processed data in memory
- **Nested Comprehensions**: Can still be memory intensive
- **Global State**: Accumulating data in global variables

## Optimization Strategies
- **Chunking**: Process data in batches
- **Streaming Algorithms**: Algorithms that work on streams
- **External Sorting**: Sort large datasets on disk
- **Memory-mapped Files**: Access large files efficiently
