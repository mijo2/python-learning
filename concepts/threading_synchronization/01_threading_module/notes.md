# Threading Module

## Overview
The `threading` module provides high-level interfaces for working with threads in Python. Threads allow concurrent execution of code, enabling programs to perform multiple operations simultaneously.

## Basic Concepts
- **Thread**: Lightweight process within a process
- **Main Thread**: Thread that starts when program begins
- **Daemon Thread**: Background thread that doesn't prevent program exit
- **Thread Safety**: Code that works correctly in multithreaded environments

## Creating Threads
```python
import threading

def worker(name):
    print(f"Worker {name} starting")
    # Do work
    print(f"Worker {name} done")

# Method 1: Function target
t = threading.Thread(target=worker, args=("A",))
t.start()
t.join()

# Method 2: Subclass
class Worker(threading.Thread):
    def run(self):
        worker(self.name)
```

## Thread Lifecycle
1. **Created**: Thread object created
2. **Started**: `start()` called, `run()` executes
3. **Running**: Code executing
4. **Terminated**: `run()` completes or exception occurs

## Thread Methods
- `start()`: Begin thread execution
- `join(timeout)`: Wait for thread to complete
- `is_alive()`: Check if thread is running
- `daemon`: Set/get daemon status
- `name`: Thread identifier

## Thread Communication
- **Global Variables**: Shared state (use with caution)
- **Queues**: Thread-safe communication
- **Events**: Synchronization primitives
- **Locks**: Prevent race conditions

## Common Patterns
- **Worker Threads**: Pool of threads processing tasks
- **Producer-Consumer**: One thread produces, another consumes
- **Background Tasks**: Daemon threads for cleanup/logging
- **Timer Threads**: Delayed execution

## Best Practices
- Keep threads simple and focused
- Use thread-safe data structures
- Avoid shared mutable state
- Handle exceptions properly
- Join threads to ensure completion
