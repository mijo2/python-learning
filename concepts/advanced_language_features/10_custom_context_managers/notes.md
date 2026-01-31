# Custom Context Managers

**Custom context managers** extend basic ones for specific needs, like logging or transactions.

## Class-Based Custom CM

```python
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
    
    def __enter__(self):
        print(f"Connecting to {self.db_name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Disconnecting from {self.db_name}")
        if exc_type:
            print(f"Error: {exc_val}")

with DatabaseConnection("mydb") as conn:
    print("Using connection")
# Disconnecting...
```

## Function-Based with contextlib

```python
from contextlib import contextmanager

@contextmanager
def suppress_errors():
    try:
        yield
    except Exception as e:
        print(f"Suppressed: {e}")

with suppress_errors():
    raise ValueError("Test")
# Suppressed: Test
```

## Advanced: Nested CM

```python
@contextmanager
def indent():
    print("  ", end="")
    yield
    print()

with indent():
    print("Indented")
```

## Best Practices

- Ensure teardown happens even on exceptions.
- Return useful objects from `__enter__`.
- Use for any resource management.

Experiment with a logging context manager. This complements functools. Next, functools utilities.