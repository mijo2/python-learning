# CPU Bound Threading Limits

The GIL limits **CPU-bound** tasks in threading. True parallelism requires multiprocessing.

## Why Limited?

- GIL serializes bytecode execution.
- Threads don't run simultaneously for CPU work.
- Overhead from context switching.

## Demonstration

CPU-bound code runs slower with threads than single-threaded.

```python
import threading
import time

def cpu_task():
    sum(i**2 for i in range(10**7))

threads = [threading.Thread(target=cpu_task) for _ in range(4)]
start = time.time()
for t in threads: t.start()
for t in threads: t.join()
print(f"Threaded time: {time.time() - start:.2f}s")  # Worse than single
```

Use multiprocessing for CPU parallelism. Threading suits I/O. Next, I/O benefits.