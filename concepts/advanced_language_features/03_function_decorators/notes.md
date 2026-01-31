# Function Decorators

**Function decorators** are a powerful way to modify or enhance functions without changing their code. They use the `@decorator` syntax.

## Basic Decorator

A decorator is a function that takes another function and returns a modified version.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def greet(name):
    return f"Hello {name}"

print(greet("Alice"))  # Before\nHello Alice\nAfter
```

## How It Works

- `@my_decorator` is syntactic sugar for `greet = my_decorator(greet)`.
- The decorator returns `wrapper`, which calls the original `func`.

## Preserving Metadata

Use `functools.wraps` to preserve `__name__`, `__doc__`, etc.

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

## Multiple Decorators

Stack decorators; applied bottom-up.

```python
@decorator1
@decorator2
def func():
    pass
# Equivalent to: decorator1(decorator2(func))
```

## Common Uses

- Logging
- Timing
- Caching
- Authorization

## Best Practices

- Use `@wraps` to preserve metadata.
- Keep decorators simple.
- Avoid side effects.

Experiment with a timing decorator. This leads to parameterized decorators. Next, class decorators.