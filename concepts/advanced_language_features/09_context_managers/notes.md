# Context Managers

**Context managers** handle setup and teardown with `with` statements, ensuring resources are managed properly.

## Basic Context Manager

```python
class FileManager:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileManager('test.txt') as f:
    f.write("Hello")
# File closed automatically
```

## How It Works

- `__enter__`: Setup, return resource.
- `__exit__`: Teardown, handle exceptions.

## contextlib Module

```python
from contextlib import contextmanager

@contextmanager
def file_manager(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

with file_manager('test.txt') as f:
    f.write("Hello")
```

## Built-in Examples

- `open()` files
- `threading.Lock()`
- Database connections

## Best Practices

- Use for resource management.
- Handle exceptions in `__exit__`.
- Prefer `contextlib` for simple cases.

Experiment with a timer context manager. This leads to custom context managers. Next, functools utilities.