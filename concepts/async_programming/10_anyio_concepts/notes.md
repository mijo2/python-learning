# AnyIO Concepts

## Overview
AnyIO is an asynchronous networking and concurrency library that provides a unified API for different async backends (asyncio, trio, curio). It allows writing async code that works across different async frameworks.

## Backend Agnostic Code
```python
import anyio

async def hello_world():
    print("Hello")
    await anyio.sleep(1)
    print("World")

# Works with any backend
anyio.run(hello_world)  # Uses asyncio by default
```

## Unified API
```python
import anyio

async def unified_example():
    # Same API regardless of backend

    # Sleeping
    await anyio.sleep(1)

    # Task groups
    async with anyio.create_task_group() as tg:
        tg.start_soon(task1)
        tg.start_soon(task2)

    # Cancellation scopes
    with anyio.CancelScope() as scope:
        await long_operation()
        scope.cancel()

    # Channels
    send, receive = anyio.create_memory_object_stream()
    await send.send("message")
    message = await receive.receive()
```

## Cross-Backend Compatibility
```python
# Code that works with asyncio, trio, or curio
async def portable_code():
    # Start tasks
    async with anyio.create_task_group() as tg:
        tg.start_soon(some_task)

    # Handle cancellation
    with anyio.CancelScope() as scope:
        await operation_that_might_be_cancelled()

    # Communicate between tasks
    sender, receiver = anyio.create_memory_object_stream(0)
    await sender.send("data")
    data = await receiver.receive()
```

## Backend Selection
```python
import anyio

# Use asyncio
anyio.run(main, backend="asyncio")

# Use trio
anyio.run(main, backend="trio")

# Auto-detect
anyio.run(main)  # Uses asyncio by default
```

## Interoperability
```python
# Mixing with backend-specific code
import asyncio
import anyio

async def mixed_code():
    # AnyIO code
    await anyio.sleep(1)

    # Backend-specific code (asyncio in this case)
    await asyncio.sleep(1)

    # More AnyIO code
    async with anyio.create_task_group() as tg:
        tg.start_soon(some_task)
```

## Key Features
- **Unified API**: Same interface across backends
- **Task Groups**: Structured concurrency
- **Cancellation**: Portable cancellation handling
- **Streams**: Memory and network streams
- **Testing**: Backend-independent testing

## Advantages
- **Portability**: Write once, run on any async backend
- **Future-Proofing**: Easy to switch backends
- **Best Practices**: Encourages structured concurrency
- **Ecosystem**: Works with libraries using different backends

## Best Practices
- Use AnyIO for new projects requiring backend flexibility
- Choose specific backend for performance-critical code
- Test with different backends
- Leverage AnyIO's high-level abstractions
