# Race Conditions

## Overview
Race conditions occur when multiple threads access shared resources concurrently, and the final outcome depends on the timing of thread execution. They can cause unpredictable and incorrect behavior.

## What Causes Race Conditions
- **Shared Mutable State**: Multiple threads modifying same data
- **Non-Atomic Operations**: Operations that aren't thread-safe
- **Timing Dependencies**: Code behavior depends on execution order

## Classic Example
```python
counter = 0

def increment():
    global counter
    temp = counter    # Read
    temp += 1         # Modify
    counter = temp    # Write

# Two threads calling increment() may both read 0,
# both write 1, losing an increment
```

## Common Race Conditions
- **Lost Updates**: One update overwrites another
- **Dirty Reads**: Reading partially updated data
- **Check-Then-Act**: Condition changes between check and action
- **Double-Checked Locking**: Unsafe optimization pattern

## Prevention Techniques
- **Locks**: Synchronize access to shared resources
- **Atomic Operations**: Use thread-safe operations
- **Immutable Data**: Use immutable objects
- **Thread-Local Storage**: Avoid shared state

## Atomic Operations
```python
import threading

counter = 0
lock = threading.Lock()

def safe_increment():
    with lock:
        global counter
        counter += 1

# Or use atomic types
from concurrent.futures import ThreadPoolExecutor
```

## Check-Then-Act Problem
```python
# Unsafe
if not shared_list:
    shared_list = []  # Race condition!

# Safe
with lock:
    if not shared_list:
        shared_list = []
```

## Testing for Race Conditions
- **Stress Testing**: Run with many threads
- **Random Delays**: Add random sleeps to expose timing issues
- **Code Review**: Look for shared state patterns
- **Static Analysis**: Use tools to detect potential races

## Debugging Race Conditions
- **Logging**: Add detailed logging of operations
- **Thread Dumps**: Analyze thread states
- **Reproducibility**: Make races deterministic for debugging
- **Isolation**: Test components separately

## Best Practices
- Minimize shared mutable state
- Use high-level synchronization primitives
- Prefer message passing over shared state
- Document thread safety guarantees
- Test thoroughly with concurrency
