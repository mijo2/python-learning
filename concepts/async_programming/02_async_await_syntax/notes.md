# Async Await Syntax

## Overview
The `async` and `await` keywords are the foundation of Python's asynchronous programming. They allow writing asynchronous code that looks synchronous, making concurrent programming more intuitive.

## Basic Syntax
```python
import asyncio

async def my_async_function():
    # Asynchronous function
    await asyncio.sleep(1)  # Non-blocking wait
    return "done"

async def main():
    result = await my_async_function()
    print(result)

# Run the async function
asyncio.run(main())
```

## Async Functions
- **Definition**: `async def function_name():`
- **Return**: Coroutines (awaitable objects)
- **Execution**: Must be awaited or run in event loop

## Await Expression
- **Purpose**: Pause execution until awaitable completes
- **Usage**: `result = await coroutine`
- **Blocking**: Only blocks the current coroutine, not the thread

## Common Awaitables
- **Coroutines**: Functions defined with `async def`
- **Tasks**: `asyncio.create_task(coroutine)`
- **Futures**: Objects that represent future results
- **Async Iterators**: Objects supporting `async for`

## Sequential vs Concurrent Execution
```python
import asyncio
import time

async def task(name, duration):
    print(f"Starting {name}")
    await asyncio.sleep(duration)
    print(f"Finished {name}")
    return f"Result {name}"

async def sequential():
    # Execute one after another
    await task("A", 1)
    await task("B", 1)
    await task("C", 1)

async def concurrent():
    # Execute simultaneously
    await asyncio.gather(
        task("A", 1),
        task("B", 1),
        task("C", 1)
    )

# Sequential: ~3 seconds
# Concurrent: ~1 second
```

## Error Handling
```python
async def risky_operation():
    try:
        result = await some_async_call()
        return result
    except ValueError as e:
        print(f"Value error: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
```

## Async Context Managers
```python
class AsyncContext:
    async def __aenter__(self):
        print("Entering context")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

async def use_context():
    async with AsyncContext() as ctx:
        await asyncio.sleep(1)
```

## Best Practices
- Use `async def` for functions that perform async operations
- Always `await` async calls
- Use `asyncio.gather()` for concurrent execution
- Handle exceptions properly
- Avoid mixing sync and async code inappropriately
