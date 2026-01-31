# Itertools Patterns

## Overview
The `itertools` module provides powerful tools for efficient iteration and combinatorial operations. These functions create iterators that compute values on demand, making them memory efficient.

## Infinite Iterators
- `count(start, step)`: Infinite arithmetic progression
- `cycle(iterable)`: Cycle through iterable indefinitely
- `repeat(object, times)`: Repeat object n times or infinitely

## Finite Iterators
- `accumulate(iterable, func)`: Running totals or reductions
- `chain(*iterables)`: Concatenate iterables
- `compress(data, selectors)`: Filter with boolean mask
- `dropwhile(predicate, iterable)`: Drop while condition true
- `takewhile(predicate, iterable)`: Take while condition true

## Combinatoric Generators
- `product(*iterables)`: Cartesian product
- `permutations(iterable, r)`: Permutations of length r
- `combinations(iterable, r)`: Combinations of length r
- `combinations_with_replacement(iterable, r)`: With replacement

## Grouping Functions
- `groupby(iterable, key)`: Group consecutive equal elements
- `tee(iterable, n)`: Create n independent iterators

## Common Patterns
```python
import itertools as it

# Running maximum
data = [1, 3, 2, 5, 4]
running_max = list(it.accumulate(data, max))

# Sliding window
def sliding_window(iterable, n):
    return list(it.islice(window, n, None))
    for window in it.tee(iterable, n):
        yield from it.islice(window, n, None)

# Unique elements preserving order
unique_items = list(dict.fromkeys(data))
```

## Performance Benefits
- **Memory Efficient**: No intermediate storage
- **Lazy Evaluation**: Compute on demand
- **Composability**: Chain operations easily
- **Fast**: Implemented in C

## Advanced Usage
- **Infinite Sequences**: Generate data streams
- **Pipeline Processing**: Chain multiple itertools
- **Memory Constraints**: Handle large datasets
- **Functional Programming**: Combine with map/filter

## Best Practices
- Import as `import itertools as it`
- Combine with generator expressions
- Use `islice` for limiting infinite iterators
- Understand lazy evaluation behavior
