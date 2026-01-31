# Trio Concepts

## Overview
Trio is an async library for Python that emphasizes structured concurrency, simplicity, and correctness. It provides a different approach to async programming compared to asyncio, with a focus on usability and safety.

## Basic Trio Usage
```python
import trio

async def hello_world():
    print("Hello")
    await trio.sleep(1)
    print("World")

trio.run(hello_world)
```

## Nursery for Concurrency
```python
import trio

async def parent():
    print("Parent starting")
    async with trio.open_nursery() as nursery:
        nursery.start_soon(child, "A")
        nursery.start_soon(child, "B")
    print("Parent finishing")

async def child(name):
    await trio.sleep(1)
    print(f"Child {name} done")

trio.run(parent)
```

## Cancellation and Timeouts
```python
import trio

async def cancellable_task():
    with trio.CancelScope() as scope:
        await trio.sleep(10)
        print("Task completed")

async def timeout_example():
    with trio.move_on_after(2) as cancel_scope:
        await cancellable_task()

    if cancel_scope.cancelled_caught:
        print("Task was cancelled due to timeout")

trio.run(timeout_example)
```

## Channels for Communication
```python
import trio

async def producer(send_channel):
    for i in range(5):
        await send_channel.send(f"Item {i}")
        await trio.sleep(0.1)

async def consumer(receive_channel):
    async for item in receive_channel:
        print(f"Received: {item}")

async def main():
    send_channel, receive_channel = trio.open_memory_channel(0)
    async with trio.open_nursery() as nursery:
        nursery.start_soon(producer, send_channel)
        nursery.start_soon(consumer, receive_channel)

trio.run(main)
```

## Exception Handling
```python
async def handle_exceptions():
    try:
        async with trio.open_nursery() as nursery:
            nursery.start_soon(successful_task)
            nursery.start_soon(failing_task)
    except ValueError as e:
        print(f"Caught exception: {e}")
        # Nursery cancelled all other tasks
```

## Comparison with asyncio
- **Structured Concurrency**: Trio enforces structured patterns
- **Simplicity**: Fewer concepts to learn
- **Safety**: Less prone to common async mistakes
- **Debugging**: Better error messages and debugging support

## Key Features
- **Nurseries**: Structured task management
- **Cancel Scopes**: Precise cancellation control
- **Channels**: Type-safe communication
- **Testing**: Built-in testing utilities

## Best Practices
- Use nurseries for concurrent tasks
- Handle cancellation properly
- Use channels for inter-task communication
- Test with Trio's testing tools
- Follow structured concurrency principles
