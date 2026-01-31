# Contextlib Helpers

## Overview
The `contextlib` module provides utilities for working with context managers. It includes decorators, context managers, and helpers for resource management.

## contextmanager Decorator
```python
from contextlib import contextmanager

@contextmanager
def database_connection(url):
    conn = create_connection(url)
    try:
        yield conn
    finally:
        conn.close()

# Usage
with database_connection("sqlite:///db.sqlite") as conn:
    conn.execute("SELECT * FROM users")
```

## closing() Context Manager
```python
from contextlib import closing

with closing(open("file.txt", "r")) as f:
    content = f.read()
# File automatically closed
```

## suppress() Context Manager
```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove("nonexistent_file")
# No exception raised if file doesn't exist
```

## redirect_stdout/stderr
```python
from contextlib import redirect_stdout, redirect_stderr
import io

# Capture stdout
output = io.StringIO()
with redirect_stdout(output):
    print("This goes to output")
print(output.getvalue())  # "This goes to output\n"
```

## ExitStack for Dynamic Context Managers
```python
from contextlib import ExitStack

def process_files(filenames):
    with ExitStack() as stack:
        files = [stack.enter_context(open(fname)) for fname in filenames]
        # All files opened, will be closed automatically
        for f in files:
            process_file(f)
```

## nullcontext
```python
from contextlib import nullcontext

# Conditional context manager
use_context = True
ctx = nullcontext() if not use_context else my_context_manager()

with ctx:
    # Code runs with or without context manager
    pass
```

## Async Context Managers
```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def async_database_connection(url):
    conn = await create_async_connection(url)
    try:
        yield conn
    finally:
        await conn.close()

# Usage
async with async_database_connection(url) as conn:
    result = await conn.execute("SELECT * FROM users")
```

## Best Practices
- Use `@contextmanager` for simple resource management
- Prefer context managers over try/finally for cleanup
- Use `ExitStack` for dynamic or multiple resources
- Handle exceptions appropriately in context managers
- Make context managers reusable
