# ParamSpec in Python

## Overview
ParamSpec allows you to preserve and manipulate the parameters of callable objects in generic contexts. It's particularly useful for decorators and higher-order functions that need to maintain the exact signature of the functions they operate on.

## Basic ParamSpec
```python
from typing import TypeVar, Callable, ParamSpec

P = ParamSpec('P')
T = TypeVar('T')

def decorator(func: Callable[P, T]) -> Callable[P, T]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result
    return wrapper

@decorator
def add(x: int, y: int) -> int:
    return x + y

# Type checker knows add has signature (int, int) -> int
result = add(1, 2)
```

## Generic Decorators
```python
from typing import ParamSpec, TypeVar, Callable, Awaitable

P = ParamSpec('P')
T = TypeVar('T')

def logged(func: Callable[P, T]) -> Callable[P, T]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@logged
def multiply(a: int, b: int, *, scale: float = 1.0) -> float:
    return a * b * scale

multiply(3, 4, scale=0.5)  # Preserves all parameters
```

## Async Decorators
```python
from typing import ParamSpec, TypeVar, Callable, Awaitable

P = ParamSpec('P')
T = TypeVar('T')

def async_logged(func: Callable[P, Awaitable[T]]) -> Callable[P, Awaitable[T]]:
    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print(f"Async call to {func.__name__}")
        result = await func(*args, **kwargs)
        print(f"Async result: {result}")
        return result
    return wrapper

@async_logged
async def fetch_data(url: str, timeout: float = 5.0) -> dict:
    # Simulate async HTTP request
    return {"url": url, "data": "response"}

# Usage preserves signature
await fetch_data("https://api.example.com", timeout=10.0)
```

## Method Decorators
```python
from typing import ParamSpec, TypeVar, Callable

P = ParamSpec('P')
T = TypeVar('T')

class MyClass:
    @staticmethod
    def method_decorator(func: Callable[P, T]) -> Callable[P, T]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            print(f"Method {func.__name__} called")
            return func(*args, **kwargs)
        return wrapper

    @method_decorator
    def my_method(self, x: int, y: str) -> str:
        return f"{x}: {y}"
```

## Complex Signatures
```python
from typing import ParamSpec, TypeVar, Callable

P = ParamSpec('P')
T = TypeVar('T')

def retry(retries: int) -> Callable[[Callable[P, T]], Callable[P, T]]:
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            for attempt in range(retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == retries:
                        raise e
                    print(f"Attempt {attempt + 1} failed: {e}")
            return None  # This line won't be reached
        return wrapper
    return decorator

@retry(3)
def unreliable_function(x: int, y: int, *, mode: str = "normal") -> int:
    if x + y > 10:
        raise ValueError("Too big")
    return x + y

# Preserves complex signature with keyword-only parameters
result = unreliable_function(3, 4, mode="special")
```

## Limitations
- ParamSpec requires Python 3.10+
- Complex interactions with other generic features
- Some type checkers may have limited support

## Best Practices
- Use ParamSpec for decorators that need to preserve signatures
- Combine with TypeVar for return type preservation
- Use for both sync and async decorators
- Keep decorators simple and focused
