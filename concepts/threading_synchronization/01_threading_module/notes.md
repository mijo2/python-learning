# Threading Module

Enter the world of concurrency! The `threading` module allows running multiple threads for parallel execution. Threads share memory, enabling efficient task parallelism.

## What is Threading?

Threads are lightweight processes within a program. Use `threading.Thread` to create them.

```python
import threading
import time

def worker(name):
    print(f"Worker {name} starting")
    time.sleep(2)
    print(f"Worker {name} done")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()  # Wait for completion

print("All done")
```

## Key Concepts

- **Thread Lifecycle**: Create, start, run, join.
- **Main Thread**: Where the program starts.
- **Daemon Threads**: Background threads that exit when main does.

## Why Threading?

- **I/O Bound Tasks**: Speed up network/file operations.
- **Responsiveness**: Keep UI responsive during tasks.
- **Shared State**: Easy data sharing.

Beware the GIL for CPU-bound tasks—use multiprocessing instead.

Experiment with simple threaded tasks!