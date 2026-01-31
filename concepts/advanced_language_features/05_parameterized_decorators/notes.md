# Parameterized Decorators

**Parameterized decorators** allow passing arguments to decorators, making them reusable and configurable.

## Basic Decorator Review

Decorators modify functions/classes.

```python
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@simple_decorator
def greet(name):
    return f"Hello {name}"
```

## Parameterized Decorators

To add parameters, create a decorator factory.

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")
```

`repeat(3)` returns the decorator, then applied to `say_hi`.

## Class-Based Parameterized Decorators

```python
class Timed:
    def __init__(self, unit="seconds"):
        self.unit = unit
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            import time
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"Time: {end - start} {self.unit}")
            return result
        return wrapper

@Timed("ms")
def slow_func():
    import time
    time.sleep(0.1)
```

## Best Practices

- Use for configurable behavior.
- Keep simple to avoid complexity.
- Test thoroughly.

Experiment with your own parameterized decorators. This enhances function decorators. Next, generators.