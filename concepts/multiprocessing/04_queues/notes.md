# Queues in Multiprocessing

## Overview
Multiprocessing queues provide thread-safe, process-safe communication between processes. They handle serialization automatically and support complex data types.

## Basic Queue Usage
```python
from multiprocessing import Process, Queue
import time

def producer(q):
    for i in range(5):
        q.put(f"Item {i}")
        print(f"Produced: Item {i}")
        time.sleep(0.1)

def consumer(q):
    while True:
        item = q.get()
        if item is None:  # Sentinel value
            break
        print(f"Consumed: {item}")
        time.sleep(0.2)

queue = Queue()

prod = Process(target=producer, args=(queue,))
cons = Process(target=consumer, args=(queue,))

prod.start()
cons.start()

prod.join()
queue.put(None)  # Signal end
cons.join()
```

## Queue Types
- **Queue**: Standard FIFO queue
- **JoinableQueue**: Supports task tracking
- **SimpleQueue**: Basic queue with less overhead

## Queue Methods
- **put(obj, block=True, timeout=None)**: Add item
- **get(block=True, timeout=None)**: Remove item
- **empty()**: Check if empty
- **full()**: Check if full
- **qsize()**: Get approximate size
- **close()**: Close queue
- **join_thread()**: Wait for background thread

## JoinableQueue for Task Tracking
```python
from multiprocessing import JoinableQueue, Process

def worker(q):
    while True:
        item = q.get()
        if item is None:
            break
        process_item(item)
        q.task_done()

queue = JoinableQueue()

workers = [Process(target=worker, args=(queue,)) for _ in range(3)]
for w in workers: w.start()

# Add tasks
for item in items:
    queue.put(item)

# Signal end
for _ in workers: queue.put(None)

# Wait for all tasks complete
queue.join()

# Stop workers
for w in workers: w.join()
```

## Producer-Consumer Pattern
```python
def producer(q, items):
    for item in items:
        q.put(item)
        print(f"Produced {item}")

def consumer(q, id):
    while True:
        item = q.get()
        if item == "STOP":
            q.put("STOP")  # Re-signal for other consumers
            break
        process_item(item)
        print(f"Consumer {id} processed {item}")
```

## Performance Considerations
- **Serialization**: Pickle/unpickle overhead
- **Buffer Size**: Internal buffer affects performance
- **Process Count**: Too many processes can hurt performance
- **Memory Usage**: Queues use shared memory

## Error Handling
```python
try:
    item = queue.get(timeout=5)
except queue.Empty:
    print("Queue empty")
except Exception as e:
    print(f"Queue error: {e}")
```

## Best Practices
- Use sentinel values to signal completion
- Handle process crashes gracefully
- Set appropriate timeouts
- Monitor queue sizes
- Close queues when done
