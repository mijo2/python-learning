# Deadlocks

## Overview
A deadlock is a situation where two or more threads are blocked forever, each waiting for resources held by the others. Deadlocks can bring applications to a complete halt.

## Coffman Conditions
Four conditions that must all be present for deadlock:
1. **Mutual Exclusion**: Resources can't be shared
2. **Hold and Wait**: Thread holds resource while waiting for another
3. **No Preemption**: Resources can't be forcibly taken
4. **Circular Wait**: Circular chain of waiting threads

## Classic Example
```python
lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    with lock1:
        time.sleep(0.1)  # Allow other thread to acquire lock2
        with lock2:      # Deadlock here
            pass

def thread2():
    with lock2:
        time.sleep(0.1)  # Allow other thread to acquire lock1
        with lock1:      # Deadlock here
            pass
```

## Detection and Prevention
- **Prevention**: Make one condition impossible
- **Avoidance**: Careful resource allocation
- **Detection**: Monitor for deadlock conditions
- **Recovery**: Kill threads or rollback operations

## Prevention Strategies
- **Lock Ordering**: Always acquire locks in same order
- **Timeout**: Use timeouts on lock acquisitions
- **Lock Hierarchy**: Assign lock numbers, acquire in order
- **Try Locks**: Use non-blocking acquisitions

## Lock Ordering Solution
```python
def safe_function():
    # Always acquire lock1 before lock2
    with lock1:
        with lock2:
            # Safe operations
```

## Timeout Prevention
```python
if lock.acquire(timeout=5.0):
    try:
        # Do work
    finally:
        lock.release()
else:
    # Handle timeout
```

## Detection Tools
- **Thread Dumps**: Analyze thread states
- **Debugging**: Add logging for lock acquisitions
- **Testing**: Stress test for deadlock conditions
- **Static Analysis**: Code analysis tools

## Common Scenarios
- **Nested Locks**: Acquiring locks in wrong order
- **Callback Deadlocks**: Callbacks acquiring same locks
- **Resource Pools**: Waiting for multiple resources
- **Complex Dependencies**: Circular dependencies

## Best Practices
- Keep lock usage simple
- Document lock ordering requirements
- Use timeouts on all blocking operations
- Test with multiple threads
- Monitor for deadlock symptoms
