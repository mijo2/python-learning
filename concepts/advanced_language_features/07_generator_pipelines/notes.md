# Generator Pipelines

**Generator pipelines** chain generators to process data streams efficiently, avoiding intermediate lists.

## Basic Pipeline

```python
def numbers():
    for i in range(10):
        yield i

def squares(nums):
    for n in nums:
        yield n ** 2

def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

pipeline = evens(squares(numbers()))
print(list(pipeline))  # [0, 4, 16, 36, 64]
```

## Benefits

- **Memory Efficient**: No intermediate storage.
- **Composable**: Easy to chain.
- **Lazy**: Process on demand.

## Using itertools

```python
from itertools import islice

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Pipeline with itertools
from itertools import takewhile
fib = takewhile(lambda x: x < 100, fibonacci())
print(list(fib))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

## Best Practices

- Keep generators simple.
- Use for data processing.
- Combine with `itertools` for power.

Experiment with text processing pipelines. This complements coroutines. Next, coroutines.