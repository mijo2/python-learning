# Locks

## Overview
Locks are synchronization primitives that prevent multiple threads from accessing shared resources simultaneously. They ensure thread safety by providing mutual exclusion.

## Lock Types
- **Lock**: Basic mutual exclusion lock
- **RLock**: Reentrant lock (can be acquired multiple times by same thread)
- **Semaphore**: Allow limited number of threads
- **Event**: Simple signaling mechanism
- **Condition**: Advanced synchronization with waiting

## Basic Lock Usage
```python
import threading

lock = threading.Lock()
shared_data = []

def worker():
    with lock:  # Acquire/release automatically
        shared_data.append(threading.current_thread().name)

# Manual acquire/release
def worker_manual():
    lock.acquire()
    try:
        shared_data.append(threading.current_thread().name)
    finally:
        lock.release()
```

## Lock Methods
- `acquire(blocking=True, timeout=-1)`: Acquire lock
- `release()`: Release lock
- `locked()`: Check if lock is held

## Reentrant Locks (RLock)
```python
rlock = threading.RLock()

def recursive_function(depth):
    with rlock:
        if depth > 0:
            recursive_function(depth - 1)  # Same thread can re-acquire
```

## Deadlock Prevention
- **Acquire in Order**: Always acquire locks in same order
- **Timeout**: Use timeouts to avoid infinite waiting
- **Try Locks**: `acquire(False)` for non-blocking
- **Lock Hierarchies**: Define lock ordering

## Common Patterns
- **Critical Sections**: Protect shared state
- **Resource Protection**: Database connections, files
- **Singleton Patterns**: Thread-safe initialization
- **Reader-Writer Locks**: Allow multiple readers, single writer

## Performance Considerations
- **Lock Contention**: Threads waiting for locks
- **Lock Granularity**: Fine vs coarse locking
- **Lock-Free Alternatives**: Atomic operations
- **Profiling**: Identify bottlenecks

## Best Practices
- Keep critical sections small
- Use context managers (`with`)
- Avoid nested locks when possible
- Document lock usage
- Test for race conditions
