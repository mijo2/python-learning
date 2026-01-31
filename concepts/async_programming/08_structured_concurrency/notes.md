# Structured Concurrency

## Overview
Structured concurrency provides a way to organize concurrent tasks with clear lifetime management, proper error propagation, and cancellation handling. It treats concurrent operations like structured programming constructs.

## Core Principles
- **Task Lifetime Management**: Child tasks don't outlive parent
- **Error Propagation**: Failures propagate to parent scope
- **Cancellation Propagation**: Cancellation affects entire task tree
- **Clear Boundaries**: Well-defined task hierarchies

## Task Groups (Python 3.11+)
```python
import asyncio

async def structured_example():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(task1())
        tg.create_task(task2())
        tg.create_task(task3())

    # All tasks complete successfully, or all cancelled on first exception

async def task1():
    await asyncio.sleep(1)
    print("Task 1 done")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 done")

async def task3():
    await asyncio.sleep(1.5)
    print("Task 3 done")
```

## Exception Handling in Task Groups
```python
async def exception_propagation():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(successful_task())
            tg.create_task(failing_task())  # Raises exception
            tg.create_task(another_task())  # Won't complete
    except Exception as e:
        print(f"Exception propagated: {e}")
        # All other tasks cancelled automatically
```

## Nursery Pattern (Alternative)
```python
class Nursery:
    def __init__(self):
        self.tasks = []
        self.exception = None

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            # Cancel all tasks on exception
            for task in self.tasks:
                if not task.done():
                    task.cancel()
            return False  # Propagate exception

        # Wait for all tasks
        await asyncio.gather(*self.tasks, return_exceptions=True)
        return False

    def create_task(self, coro):
        task = asyncio.create_task(coro)
        self.tasks.append(task)
        return task
```

## Cancellation Propagation
```python
async def cancellation_example():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(long_running_task())
        tg.create_task(short_task())

    # If short_task fails, long_running_task is cancelled
```

## Comparison with Unstructured Concurrency
```python
# Unstructured (problematic)
async def unstructured():
    task1 = asyncio.create_task(work1())
    task2 = asyncio.create_task(work2())

    # What if exception occurs here?
    result1 = await task1

    # task2 might still be running...

# Structured (better)
async def structured():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(work1())
        tg.create_task(work2())
    # All tasks complete or all cancelled
```

## Resource Management
```python
async def resource_example():
    async with acquire_resource() as resource:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(use_resource(resource, "task1"))
            tg.create_task(use_resource(resource, "task2"))
        # Resource still held here

    # Resource released after task group
```

## Timeout Handling
```python
async def timeout_example():
    try:
        async with asyncio.timeout(5.0):
            async with asyncio.TaskGroup() as tg:
                tg.create_task(task1())
                tg.create_task(task2())
    except asyncio.TimeoutError:
        print("Operation timed out")
        # All tasks cancelled automatically
```

## Best Practices
- Use TaskGroup for concurrent operations
- Handle exceptions at appropriate levels
- Ensure proper resource cleanup
- Use timeouts to prevent hanging
- Test cancellation scenarios
- Prefer structured over unstructured concurrency
