# Thread Pools

## Overview
Thread pools manage a collection of reusable threads, providing efficient thread management and workload distribution. They help avoid the overhead of creating and destroying threads frequently.

## Why Thread Pools?
- **Performance**: Reuse threads instead of creating new ones
- **Resource Control**: Limit number of concurrent threads
- **Task Management**: Queue tasks when all threads busy
- **Cleanup**: Proper thread lifecycle management

## concurrent.futures.ThreadPoolExecutor
```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def worker(task_id):
    time.sleep(1)  # Simulate work
    return f"Task {task_id} completed"

with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks
    futures = [executor.submit(worker, i) for i in range(5)]

    # Process results as they complete
    for future in as_completed(futures):
        print(future.result())
```

## Pool Configuration
- **max_workers**: Maximum concurrent threads (default: CPU count * 5)
- **thread_name_prefix**: Naming for debugging
- **initializer**: Function to run in each thread
- **initargs**: Arguments for initializer

## Task Submission
- **submit(fn, *args, **kwargs)**: Submit task, get Future
- **map(fn, iterable, timeout)**: Apply function to each item
- **shutdown(wait=True)**: Clean shutdown

## Future Objects
- **result(timeout)**: Get result (blocks)
- **exception(timeout)**: Get exception if raised
- **done()**: Check if completed
- **cancel()**: Try to cancel task
- **add_done_callback(fn)**: Callback when done

## Error Handling
```python
def risky_task():
    if random.random() < 0.5:
        raise ValueError("Random error")
    return "Success"

with ThreadPoolExecutor() as executor:
    future = executor.submit(risky_task)
    try:
        result = future.result(timeout=5)
    except concurrent.futures.TimeoutError:
        print("Task timed out")
    except Exception as e:
        print(f"Task failed: {e}")
```

## Advanced Patterns
- **Batch Processing**: Process items in parallel batches
- **Pipeline Processing**: Chain thread pool operations
- **Work Stealing**: Threads can steal work from others
- **Priority Queues**: Tasks with different priorities

## Performance Tuning
- **Pool Size**: Balance CPU cores and I/O wait time
- **Task Granularity**: Tasks should be substantial
- **Monitoring**: Track pool utilization
- **Scaling**: Adjust pool size dynamically

## Best Practices
- Use context managers for automatic cleanup
- Handle exceptions properly
- Set appropriate timeouts
- Monitor thread pool metrics
- Avoid blocking operations in threads
