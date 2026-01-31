# Process Pools

**Process pools** manage a pool of worker processes for parallel execution, bypassing GIL for CPU-bound tasks.

## What is a Process Pool?

A pool of processes that can execute tasks concurrently.

```python
from multiprocessing import Pool

def square(x):
    return x * x

with Pool(4) as p:
    results = p.map(square, [1, 2, 3, 4])
    print(results)  # [1, 4, 9, 16]
```

## Key Features

- **map**: Apply function to iterable in parallel.
- **apply_async**: Asynchronous task execution.
- **close/join**: Manage pool lifecycle.

## When to Use?

- CPU-intensive tasks needing parallelism.
- Batch processing.

## Best Practices

- Use context manager for automatic cleanup.
- Choose pool size based on CPU cores.
- Handle exceptions in worker functions.

Experiment with Pool for parallel computation. This extends multiprocessing module. Next, pipes.