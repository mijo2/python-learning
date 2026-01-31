# Semaphores

## Overview
Semaphores are synchronization primitives that control access to a shared resource by maintaining a counter. They allow a limited number of threads to access a resource simultaneously.

## Types of Semaphores
- **Counting Semaphore**: Allows n threads simultaneously
- **Binary Semaphore**: Allows 0 or 1 (similar to lock)
- **Bounded Semaphore**: Prevents more releases than acquires

## Basic Usage
```python
import threading

# Allow 3 threads simultaneously
semaphore = threading.Semaphore(3)

def worker():
    with semaphore:
        print(f"Thread {threading.current_thread().name} working")
        # Do work
        print(f"Thread {threading.current_thread().name} done")

threads = [threading.Thread(target=worker) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

## Semaphore Methods
- `acquire(blocking=True, timeout=-1)`: Decrement counter
- `release()`: Increment counter
- `get_value()`: Get current counter value (Python 3.9+)

## Producer-Consumer Pattern
```python
empty = threading.Semaphore(10)  # Buffer slots
full = threading.Semaphore(0)    # Items in buffer
mutex = threading.Lock()

def producer():
    while True:
        item = produce_item()
        empty.acquire()  # Wait for empty slot
        with mutex:
            buffer.append(item)
        full.release()   # Signal item available

def consumer():
    while True:
        full.acquire()   # Wait for item
        with mutex:
            item = buffer.pop(0)
        empty.release()  # Signal slot available
        consume_item(item)
```

## Use Cases
- **Resource Limits**: Limit concurrent connections
- **Buffer Management**: Producer-consumer problems
- **Rate Limiting**: Control operation frequency
- **Pool Management**: Database connections, threads

## Bounded Semaphore
```python
bounded_sem = threading.BoundedSemaphore(5)

# Prevents too many releases
bounded_sem.acquire()
bounded_sem.release()  # OK
# bounded_sem.release()  # Would raise ValueError
```

## Performance Considerations
- **Contention**: Threads waiting for semaphore
- **Fairness**: FIFO vs priority ordering
- **Overhead**: Semaphore operations have cost
- **Starvation**: Threads waiting indefinitely

## Best Practices
- Initialize with appropriate value
- Use context managers
- Handle exceptions properly
- Document resource limits
- Monitor semaphore usage
