# Memoization Patterns

## Overview
Memoization is a technique to cache the results of expensive function calls and return the cached result when the same inputs occur again. This optimization can significantly improve performance for recursive functions or functions with repeated computations.

## How Memoization Works
- Store function results in a cache (dictionary) keyed by function arguments
- Check cache before computation
- Return cached value if available, otherwise compute and store

## Built-in Memoization
- `functools.lru_cache`: Decorator for least recently used caching
- `functools.cache`: Unlimited cache (Python 3.9+)

## Manual Memoization
```python
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
```

## Advanced Patterns
- **LRU Cache**: Limited size, evicts least recently used
- **TTL Cache**: Time-to-live expiration
- **Memoization with Keys**: Custom key functions
- **Recursive Memoization**: For dynamic programming

## Use Cases
- Fibonacci sequences
- Expensive computations (API calls, database queries)
- Recursive algorithms
- Pure functions with repeated inputs

## Considerations
- Memory usage for large caches
- Thread safety
- Cache invalidation
- Hashable arguments requirement
