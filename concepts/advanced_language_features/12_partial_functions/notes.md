# Partial Functions

**Partial functions** fix some arguments of a function, creating a new function with fewer parameters. From `functools.partial`.

## Basic Usage

```python
from functools import partial

def add(a, b, c):
    return a + b + c

add_five = partial(add, 5)
print(add_five(3, 2))  # 10 (5 + 3 + 2)
```

## Keyword Arguments

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

formal_greet = partial(greet, greeting="Good day")
print(formal_greet("Alice"))  # Good day, Alice!
```

## Use Cases

- Default configurations
- Callback functions
- Reducing parameters

## Comparison to Lambdas

```python
# Partial
add_ten = partial(add, 10)

# Lambda
add_ten_lambda = lambda b, c: add(10, b, c)
```

Partials are more efficient for repeated use.

## Best Practices

- Use when you need variants of a function.
- Combine with higher-order functions.
- Prefer over lambdas for complex cases.

Experiment with partial for sorting or mapping. This leads to memoization. Next, memoization patterns.