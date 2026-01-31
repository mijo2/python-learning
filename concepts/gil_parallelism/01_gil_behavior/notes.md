# GIL Behavior

Welcome to concurrency! The **Global Interpreter Lock (GIL)** is Python's mechanism that allows only one thread to execute Python bytecode at a time. It's crucial for understanding threading limitations in CPython.

## What is the GIL?

A mutex that protects Python's internal state. Only one thread runs Python code simultaneously—others wait.

- **Why?** Simplifies memory management (no reference counting locks).
- **Impact**: CPU-bound threads don't parallelize—serialized execution.

```python
import threading
import time

def cpu_task():
    sum(i for i in range(10**7))  # CPU-bound

threads = [threading.Thread(target=cpu_task) for _ in range(4)]
start = time.time()
for t in threads: t.start()
for t in threads: t.join()
print(f"Time: {time.time() - start:.2f}s")  # Slower than single-threaded!
```

GIL serializes CPU work—use multiprocessing for parallelism.

## How GIL Works

- **Release on I/O**: GIL released during blocking I/O (network, file).
- **Periodic Release**: Threads switch every ~15ms or 100 bytecode instructions.
- **Extensions**: C extensions can release GIL for true parallelism.

## Implications

- **Threading for I/O**: Great for web servers (wait for responses).
- **Multiprocessing for CPU**: Bypass GIL with processes.
- **Async for Concurrency**: Non-blocking I/O without threads.

Experiment with CPU vs. I/O tasks. Measure performance. This explains why Python threading differs from other languages. Next, CPU-bound limits.