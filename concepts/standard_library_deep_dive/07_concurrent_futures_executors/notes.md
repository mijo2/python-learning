# Concurrent Futures Executors

## Overview
The `concurrent.futures` module provides high-level interfaces for asynchronously executing callable objects. It includes ThreadPoolExecutor and ProcessPoolExecutor for parallel execution.

## ThreadPoolExecutor
```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def worker(task_id):
    time.sleep(1)  # Simulate IO-bound work
    return f"Task {task_id} completed"

# Execute tasks concurrently
with ThreadPoolExecutor(max_workers=4) as executor:
    # Submit tasks
    futures = [executor.submit(worker, i) for i in range(10)]

    # Process results as they complete
    for future in as_completed(futures):
        print(future.result())
```

## ProcessPoolExecutor
```python
from concurrent.futures import ProcessPoolExecutor

def cpu_intensive(n):
    return sum(i*i for i in range(n))

# Use processes for CPU-bound tasks
with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(cpu_intensive, [100000] * 8))
    print(f"Results: {results}")
```

## Future Objects
```python
# Submit and handle individual futures
future = executor.submit(long_running_task, arg1, arg2)

# Check status
print(f"Done: {future.done()}")
print(f"Running: {future.running()}")

# Get result (blocking)
try:
    result = future.result(timeout=10)
    print(f"Result: {result}")
except concurrent.futures.TimeoutError:
    print("Task timed out")
except Exception as e:
    print(f"Task failed: {e}")

# Cancel if possible
if not future.done():
    cancelled = future.cancel()
    print(f"Cancelled: {cancelled}")
```

## Map Function
```python
# Apply function to each item
def square(x):
    return x * x

with ThreadPoolExecutor() as executor:
    results = list(executor.map(square, range(10)))
    print(results)  # [0, 1, 4, 9, 16, ...]
```

## Exception Handling
```python
def risky_task(x):
    if x == 5:
        raise ValueError("Bad input")
    return x * 2

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(risky_task, i) for i in range(10)]

    for future in as_completed(futures):
        try:
            result = future.result()
            print(f"Success: {result}")
        except ValueError as e:
            print(f"Failed: {e}")
```

## Callbacks
```python
def on_completion(future):
    try:
        result = future.result()
        print(f"Task completed: {result}")
    except Exception as e:
        print(f"Task failed: {e}")

future = executor.submit(worker, 1)
future.add_done_callback(on_completion)
```

## Choosing Executor Type
- **ThreadPoolExecutor**: IO-bound tasks, shared memory
- **ProcessPoolExecutor**: CPU-bound tasks, avoid GIL
- **ThreadPoolExecutor**: Lower overhead, easier debugging
- **ProcessPoolExecutor**: True parallelism, higher memory usage

## Best Practices
- Use context managers for automatic cleanup
- Set appropriate max_workers
- Handle exceptions properly
- Use timeouts to prevent hanging
- Choose executor based on task type
