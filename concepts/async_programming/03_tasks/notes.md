# Tasks in Async Programming

## Overview
Tasks are the primary way to run and manage concurrent coroutines in asyncio. They represent asynchronous operations that can be scheduled, cancelled, and monitored.

## Creating Tasks
```python
import asyncio

async def my_coroutine(name, delay):
    await asyncio.sleep(delay)
    return f"Task {name} completed"

async def main():
    # Create tasks
    task1 = asyncio.create_task(my_coroutine("A", 1))
    task2 = asyncio.create_task(my_coroutine("B", 2))

    # Wait for completion
    result1 = await task1
    result2 = await task2

    print(result1, result2)

asyncio.run(main())
```

## Task Lifecycle
1. **Created**: Task object created
2. **Pending**: Waiting to run or running
3. **Done**: Completed successfully or with exception
4. **Cancelled**: Cancelled before completion

## Task Methods
- **done()**: Check if task completed
- **result()**: Get result (raises exception if failed)
- **exception()**: Get exception if task failed
- **cancel()**: Request cancellation
- **cancelled()**: Check if cancelled

## Gathering Results
```python
async def gather_example():
    tasks = [
        asyncio.create_task(my_coroutine(f"Task{i}", i))
        for i in range(1, 4)
    ]

    # Wait for all to complete
    results = await asyncio.gather(*tasks)
    print(results)

    # Or process as they complete
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(f"Completed: {result}")
```

## Task Cancellation
```python
async def cancellable_task():
    try:
        await asyncio.sleep(10)
        return "Completed"
    except asyncio.CancelledError:
        print("Task was cancelled")
        raise  # Re-raise to propagate cancellation

async def main():
    task = asyncio.create_task(cancellable_task())

    await asyncio.sleep(2)
    task.cancel()  # Request cancellation

    try:
        result = await task
    except asyncio.CancelledError:
        print("Task cancelled successfully")
```

## Task Groups (Python 3.11+)
```python
async def task_group_example():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(my_coroutine("A", 1))
        tg.create_task(my_coroutine("B", 2))
        tg.create_task(my_coroutine("C", 1.5))

    # All tasks complete or all cancelled on exception
```

## Background Tasks
```python
async def background_worker():
    while True:
        await asyncio.sleep(1)
        print("Background work")

async def main():
    # Start background task
    background_task = asyncio.create_task(background_worker())

    # Do main work
    await asyncio.sleep(5)

    # Cancel background task
    background_task.cancel()
    try:
        await background_task
    except asyncio.CancelledError:
        pass
```

## Task Scheduling
```python
async def scheduled_task():
    # Run every 2 seconds
    while True:
        await asyncio.sleep(2)
        print("Scheduled task executed")

# Add to event loop
asyncio.create_task(scheduled_task())
```

## Error Handling
```python
async def handle_task_errors():
    tasks = [
        asyncio.create_task(risky_operation())
        for _ in range(3)
    ]

    for task in asyncio.as_completed(tasks):
        try:
            result = await task
            print(f"Success: {result}")
        except Exception as e:
            print(f"Task failed: {e}")
```

## Best Practices
- Use `asyncio.create_task()` to schedule coroutines
- Handle task cancellation properly
- Use `asyncio.gather()` for waiting on multiple tasks
- Monitor task states when debugging
- Cancel tasks to prevent resource leaks
