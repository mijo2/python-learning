# Producer Consumer Queues

## Overview
Producer-consumer is a classic concurrency pattern where producer threads create work items and consumer threads process them. Queues provide the communication mechanism between producers and consumers.

## Basic Pattern
```python
import queue
import threading
import time

work_queue = queue.Queue()

def producer():
    for i in range(10):
        work_queue.put(f"Task {i}")
        print(f"Produced: Task {i}")
        time.sleep(0.1)

def consumer():
    while True:
        try:
            task = work_queue.get(timeout=1)
            print(f"Consumed: {task}")
            work_queue.task_done()
        except queue.Empty:
            break

# Start threads
prod_thread = threading.Thread(target=producer)
cons_thread = threading.Thread(target=consumer)

prod_thread.start()
cons_thread.start()

prod_thread.join()
cons_thread.join()
```

## Queue Types
- **Queue**: FIFO queue
- **LifoQueue**: LIFO (stack)
- **PriorityQueue**: Items with priorities

## Queue Methods
- **put(item, block=True, timeout=None)**: Add item
- **get(block=True, timeout=None)**: Remove item
- **empty()**: Check if empty
- **full()**: Check if full
- **qsize()**: Get size
- **task_done()**: Mark task complete
- **join()**: Wait for all tasks done

## Thread-Safe Operations
```python
# Safe for multiple producers/consumers
queue = queue.Queue(maxsize=100)

# Multiple producers
def producer(id):
    for i in range(5):
        queue.put(f"P{id}-Task{i}")

# Multiple consumers
def consumer(id):
    while True:
        try:
            task = queue.get(timeout=1)
            print(f"C{id}: {task}")
            queue.task_done()
        except queue.Empty:
            break
```

## Advanced Patterns
- **Bounded Queues**: Limit queue size for backpressure
- **Poison Pills**: Special items to signal termination
- **Work Pools**: Multiple consumers sharing work
- **Pipeline**: Chain producer-consumer stages

## Error Handling
```python
def safe_consumer():
    while True:
        try:
            item = work_queue.get(timeout=5)
            process_item(item)
        except queue.Empty:
            continue  # Keep waiting
        except Exception as e:
            print(f"Processing error: {e}")
        finally:
            work_queue.task_done()
```

## Performance Considerations
- **Queue Size**: Balance memory usage and throughput
- **Blocking**: Use timeouts to prevent deadlocks
- **Batch Processing**: Get multiple items at once
- **Monitoring**: Track queue size and processing rates

## Best Practices
- Use appropriate queue types
- Handle exceptions gracefully
- Implement proper shutdown signals
- Monitor queue health
- Test with different producer/consumer ratios
