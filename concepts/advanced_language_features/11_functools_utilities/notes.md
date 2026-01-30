# functools Utilities

The `functools` module provides higher-order functions for functional programming, like partial application and caching.

## partial

Fix arguments to create new functions.

```python
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)

print(square(5))  # 25
print(cube(5))    # 125
```

## lru_cache

Memoize function results.

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # Fast after first call
```

## reduce

Apply function cumulatively.

```python
from functools import reduce

nums = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, nums)  # 10
```

## Other Utilities

- `cmp_to_key`: For sorting with custom comparers.
- `total_ordering`: Auto-add comparison methods.
- `singledispatch`: Single dispatch generic functions.

## Best Practices

- Use `lru_cache` for expensive computations.
- `partial` for creating variants.
- `reduce` for accumulations.

Experiment with caching recursive functions. This leads to partial functions. Next, partial functions.