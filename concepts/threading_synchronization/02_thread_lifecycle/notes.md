# Thread Lifecycle

## Overview
Understanding the thread lifecycle is crucial for writing robust multithreaded applications. Each thread goes through several states from creation to termination.

## Thread States
1. **New**: Thread created but not started
2. **Runnable**: Thread ready to run, waiting for CPU
3. **Running**: Thread currently executing
4. **Blocked**: Thread waiting for resource or event
5. **Terminated**: Thread completed execution

## Lifecycle Methods
- `threading.Thread()`: Create thread object
- `start()`: Transition to runnable state
- `run()`: Execute thread code (called by start)
- `join()`: Wait for thread completion
- `is_alive()`: Check if thread is still running

## Detailed Lifecycle
```python
import threading
import time

def worker():
    print("Thread starting")
    time.sleep(1)  # Simulates work
    print("Thread finishing")

thread = threading.Thread(target=worker)

# State: New
print(f"Created: {thread.is_alive()}")

thread.start()  # State: Runnable -> Running
print(f"Started: {thread.is_alive()}")

thread.join()  # Wait for completion
print(f"Joined: {thread.is_alive()}")  # State: Terminated
```

## Blocking Operations
- **I/O Operations**: Reading files, network calls
- **Sleep**: `time.sleep()`
- **Join**: Waiting for other threads
- **Locks**: Waiting for synchronization primitives
- **Queues**: Waiting for items

## Thread Termination
- **Normal Termination**: `run()` method completes
- **Exception Termination**: Unhandled exception in thread
- **Forced Termination**: Not recommended, use flags instead

## Daemon Threads
```python
thread = threading.Thread(target=worker)
thread.daemon = True  # Thread won't prevent program exit
thread.start()
```

## Thread Pools
- **ThreadPoolExecutor**: Manage pool of threads
- **Reusing Threads**: Avoid creation overhead
- **Task Submission**: Submit tasks to pool
- **Shutdown**: Clean termination of pool

## Monitoring Threads
- `threading.enumerate()`: List all active threads
- `threading.active_count()`: Number of active threads
- `threading.current_thread()`: Current thread object
- Thread names and identifiers
