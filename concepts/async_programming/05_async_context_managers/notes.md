# Async Context Managers

## Overview
Async context managers provide a way to manage resources in asynchronous code, ensuring proper setup and cleanup of resources like database connections, file handles, or network sockets.

## Basic Syntax
```python
class AsyncResource:
    async def __aenter__(self):
        print("Setting up resource")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Cleaning up resource")

async def use_resource():
    async with AsyncResource() as resource:
        print("Using resource")
        await asyncio.sleep(1)  # Simulate async operation
    # Resource automatically cleaned up here
```

## Async Context Manager Protocol
- **`__aenter__(self)`**: Called on entry, returns resource
- **`__aexit__(self, exc_type, exc_val, exc_tb)`**: Called on exit, handles cleanup

## Decorator Approach
```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def async_resource_manager():
    print("Setup")
    resource = "my resource"
    try:
        yield resource
    finally:
        print("Cleanup")

async def use_decorator():
    async with async_resource_manager() as res:
        print(f"Using {res}")
```

## Real-world Examples
```python
# Database connection
class DatabaseConnection:
    async def __aenter__(self):
        self.connection = await create_db_connection()
        return self.connection

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.connection.close()

async def query_database():
    async with DatabaseConnection() as conn:
        results = await conn.execute("SELECT * FROM users")
        return results

# File operations
@asynccontextmanager
async def async_open_file(filename, mode):
    file = await aiofiles.open(filename, mode)
    try:
        yield file
    finally:
        await file.close()

async def process_file():
    async with async_open_file("data.txt", "r") as f:
        content = await f.read()
        return content
```

## Exception Handling
```python
async def exception_example():
    async with AsyncResource() as res:
        if random.random() < 0.5:
            raise ValueError("Something went wrong")

    # __aexit__ still called even if exception occurs
```

## Nested Context Managers
```python
async def nested_example():
    async with AsyncResource() as res1:
        async with AsyncResource() as res2:
            # Both resources available
            pass
        # res2 cleaned up, res1 still available
    # res1 cleaned up
```

## Async Context Managers with asyncio
```python
# Timeout context manager
@asynccontextmanager
async def async_timeout(seconds):
    task = None
    try:
        yield
    finally:
        if task and not task.done():
            task.cancel()

async def timeout_example():
    async with async_timeout(5):
        await asyncio.sleep(10)  # Will be cancelled after 5 seconds
```

## Stack Management
```python
# Managing multiple resources
@asynccontextmanager
async def multi_resource():
    res1 = await acquire_resource1()
    res2 = await acquire_resource2()
    try:
        yield (res1, res2)
    finally:
        await release_resource2(res2)
        await release_resource1(res1)
```

## Best Practices
- Always implement both `__aenter__` and `__aexit__`
- Handle exceptions in `__aexit__`
- Use `@asynccontextmanager` for simple cases
- Ensure cleanup happens even on exceptions
- Test resource management thoroughly
