# Condition Variables

## Overview
Condition variables provide a way for threads to wait for certain conditions to become true. They are used in conjunction with locks to coordinate thread execution based on state changes.

## Basic Concept
- **Wait**: Thread waits for condition to be met
- **Notify**: Thread signals that condition has changed
- **Broadcast**: Wake up all waiting threads

## Usage Pattern
```python
import threading

condition = threading.Condition()
shared_data = []
max_items = 10

def producer():
    while True:
        with condition:
            while len(shared_data) >= max_items:
                condition.wait()  # Wait for space
            shared_data.append("item")
            condition.notify()  # Notify consumer

def consumer():
    while True:
        with condition:
            while not shared_data:
                condition.wait()  # Wait for items
            item = shared_data.pop(0)
            condition.notify()  # Notify producer
```

## Condition Methods
- `wait(timeout=None)`: Wait for notification
- `notify(n=1)`: Wake up n waiting threads
- `notify_all()`: Wake up all waiting threads
- `acquire()` / `release()`: Lock management

## Wait Mechanics
- **Atomic Release and Wait**: Releases lock and waits atomically
- **Re-acquire on Wake**: Automatically re-acquires lock when notified
- **Spurious Wakeups**: May wake without notification (check condition)

## Producer-Consumer Example
```python
class BoundedBuffer:
    def __init__(self, size):
        self.buffer = []
        self.size = size
        self.condition = threading.Condition()

    def put(self, item):
        with self.condition:
            while len(self.buffer) >= self.size:
                self.condition.wait()
            self.buffer.append(item)
            self.condition.notify()

    def get(self):
        with self.condition:
            while not self.buffer:
                self.condition.wait()
            item = self.buffer.pop(0)
            self.condition.notify()
            return item
```

## Common Patterns
- **Barrier**: Wait for all threads to reach a point
- **Event Simulation**: Wait for events with additional logic
- **Resource Pools**: Wait for available resources
- **Work Queues**: Wait for work items

## Best Practices
- Always check condition after wait (spurious wakeups)
- Use while loops, not if statements
- Minimize time spent holding lock
- Prefer notify() over notify_all() when possible
- Document condition variable usage
