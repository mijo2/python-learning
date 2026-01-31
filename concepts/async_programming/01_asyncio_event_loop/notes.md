# Asyncio Event Loop

**Asyncio** enables asynchronous programming for concurrent I/O without threads. The **event loop** orchestrates coroutines—functions that can pause and resume.

## What is Asyncio?

Handles I/O concurrently using `async`/`await`. Single-threaded, event-driven.

```python
import asyncio

async def greet(name):
    print(f"Hello {name}")
    await asyncio.sleep(1)  # Non-blocking pause
    print(f"Goodbye {name}")

async def main():
    await asyncio.gather(greet("Alice"), greet("Bob"))  # Concurrent

asyncio.run(main())
```

`asyncio.run()` starts the event loop, running coroutines concurrently.

## Event Loop Mechanics

- **Single Thread**: No GIL issues.
- **Cooperative**: Coroutines yield control via `await`.
- **I/O Ready**: Pauses on I/O, resumes when ready.

## Key Concepts

- **async def**: Defines coroutine.
- **await**: Pauses until awaited task completes.
- **asyncio.gather()**: Runs multiple coroutines concurrently.

## Why Async?

- **Scalability**: Handle thousands of connections.
- **Efficiency**: No thread overhead.
- **Simplicity**: For I/O-bound apps.

Experiment with `asyncio.sleep()` and `gather()`. This is the foundation of async Python—next, async/await syntax.