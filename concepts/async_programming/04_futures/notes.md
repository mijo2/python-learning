# Futures in Async Programming

## Overview
Futures represent the result of asynchronous operations that may not be available yet. They provide a way to access results of concurrent operations and handle completion callbacks.

## Basic Future Usage
```python
import asyncio
import concurrent.futures

def blocking_operation(x):
    import time
    time.sleep(1)
    return x * 2

async def main():
    # Run blocking operation in thread pool
    loop = asyncio.get_running_loop()

    # Submit to thread pool
    future = loop.run_in_executor(None, blocking_operation, 5)

    # Wait for result
    result = await future
    print(f"Result: {result}")

asyncio.run(main())
```

## Future States
- **Pending**: Operation not yet complete
- **Running**: Operation in progress
- **Done**: Operation completed (success or failure)
- **Cancelled**: Operation was cancelled

## Future Methods
- **done()**: Check if operation completed
- **result()**: Get result (blocks if not done)
- **exception()**: Get exception if operation failed
- **cancel()**: Attempt to cancel operation
- **cancelled()**: Check if operation was cancelled
- **add_done_callback(fn)**: Add callback for completion

## Creating Custom Futures
```python
async def custom_future_example():
    future = asyncio.Future()

    # Simulate async operation
    async def set_result():
        await asyncio.sleep(1)
        future.set_result("Operation complete")

    # Start operation
    asyncio.create_task(set_result())

    # Wait for result
    result = await future
    print(result)

asyncio.run(custom_future_example())
```

## Future Callbacks
```python
def on_complete(future):
    try:
        result = future.result()
        print(f"Operation succeeded: {result}")
    except Exception as e:
        print(f"Operation failed: {e}")

async def callback_example():
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, blocking_operation, 10)

    # Add callback
    future.add_done_callback(on_complete)

    # Do other work while waiting
    await asyncio.sleep(0.5)
    print("Doing other work...")

    # Wait for completion if needed
    await future
```

## Converting to Tasks
```python
async def future_to_task():
    # Create future
    future = asyncio.Future()

    # Convert to task for better integration
    task = asyncio.create_task(future)

    # Or wrap in task
    async def wrapper():
        return await future

    task = asyncio.create_task(wrapper())
```

## Exception Handling
```python
async def handle_future_exceptions():
    future = asyncio.Future()

    # Simulate failure
    async def fail_operation():
        await asyncio.sleep(1)
        future.set_exception(ValueError("Operation failed"))

    asyncio.create_task(fail_operation())

    try:
        result = await future
    except ValueError as e:
        print(f"Caught exception: {e}")
```

## Integration with Thread Pools
```python
async def thread_pool_example():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        loop = asyncio.get_running_loop()

        # Submit multiple operations
        futures = [
            loop.run_in_executor(executor, blocking_operation, i)
            for i in range(5)
        ]

        # Wait for all
        results = await asyncio.gather(*futures)
        print(f"Results: {results}")
```

## Best Practices
- Use futures for integrating blocking operations
- Handle exceptions properly
- Add callbacks for non-blocking completion handling
- Use `asyncio.gather()` for multiple futures
- Prefer tasks for pure async operations
