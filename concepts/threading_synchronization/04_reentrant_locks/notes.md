# Reentrant Locks

## Overview
Reentrant locks (RLocks) allow the same thread to acquire the lock multiple times without blocking. This is useful for recursive functions or when a thread needs to call functions that also acquire the same lock.

## Difference from Regular Locks
- **Lock**: Thread blocks if it tries to acquire already held lock
- **RLock**: Thread can acquire multiple times, tracks ownership count

## Basic Usage
```python
import threading

rlock = threading.RLock()

def recursive_worker(depth):
    with rlock:
        print(f"Depth {depth}")
        if depth > 0:
            recursive_worker(depth - 1)  # Can re-acquire same lock

threading.Thread(target=recursive_worker, args=(3,)).start()
```

## How It Works
- **Ownership Tracking**: Tracks which thread owns the lock
- **Reference Counting**: Counts acquisition levels
- **Release Matching**: Must release same number of times as acquired

## Internal Mechanism
```python
class RLock:
    def __init__(self):
        self._owner = None
        self._count = 0
        self._lock = threading.Lock()

    def acquire(self):
        if self._owner == threading.current_thread():
            self._count += 1
            return True
        # Regular acquisition logic
```

## Use Cases
- **Recursive Functions**: Functions that call themselves
- **Callback Systems**: Callbacks that may trigger more callbacks
- **Object Methods**: Methods that call other methods on same object
- **Complex Call Chains**: Deep method call hierarchies

## Advantages
- **Prevents Deadlock**: In recursive scenarios
- **Cleaner Code**: No need to track lock state manually
- **Thread Safety**: Same thread can safely re-enter

## Disadvantages
- **Performance**: Slight overhead compared to regular locks
- **Debugging**: Harder to track lock usage
- **Misuse**: Can hide design problems

## Best Practices
- Use when recursion is necessary
- Prefer regular locks when possible
- Document reentrant usage
- Avoid excessive nesting
- Test thoroughly for correct release
