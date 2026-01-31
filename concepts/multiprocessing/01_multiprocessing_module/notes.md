# Multiprocessing Module

To bypass GIL limitations, use **multiprocessing** for true parallelism with separate processes. Each process has its own GIL and memory space.

## What is Multiprocessing?

Runs tasks in separate OS processes—true CPU parallelism.

```python
from multiprocessing import Process
import time

def worker(name):
    print(f"Worker {name} starting")
    time.sleep(2)
    print(f"Worker {name} done")

processes = []
for i in range(4):
    p = Process(target=worker, args=(i,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

print("All done")
```

Processes run concurrently—faster for CPU tasks.

## Key Features

- **Process Class**: Like threading.Thread.
- **Pool**: Manage worker processes.
- **Queues/Pipes**: Inter-process communication.
- **Shared Memory**: For data sharing.

## When to Use?

- CPU-bound tasks needing parallelism.
- Heavy computations.
- Bypassing GIL.

## Pitfalls

- **Overhead**: Process creation is expensive.
- **Serialization**: Data must be pickled.
- **No Shared State**: Use queues for communication.

Experiment with Process vs. Thread for CPU tasks. Measure speedup. This unlocks parallel computing in Python!