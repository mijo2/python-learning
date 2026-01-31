# Pickle Serialization Costs

## Overview
Multiprocessing uses pickle to serialize objects for inter-process communication. Understanding pickle's performance characteristics and costs is crucial for optimizing multiprocessing applications.

## What is Pickle?
- **Purpose**: Convert Python objects to byte streams
- **Used By**: Queues, Pipes, Manager objects
- **Automatic**: Happens transparently in multiprocessing

## Serialization Costs
```python
import pickle
import time
from multiprocessing import Queue, Process

# Test serialization cost
data = {"large": list(range(10000)), "nested": {"a": [1,2,3] * 100}}

# Measure pickle time
start = time.time()
pickled = pickle.dumps(data)
pickle_time = time.time() - start

start = time.time()
unpickled = pickle.loads(pickled)
unpickle_time = time.time() - start

print(f"Pickle: {pickle_time:.4f}s, Unpickle: {unpickle_time:.4f}s")
print(f"Size: {len(pickled)} bytes")
```

## Performance Impact
- **Large Objects**: Expensive to serialize
- **Complex Objects**: Deep nesting increases cost
- **Frequent Communication**: Serialization overhead accumulates
- **Memory Usage**: Pickled data can be larger

## Optimization Strategies
```python
# Use shared memory for large data
from multiprocessing import Array, Value

# Instead of passing large lists via queue
shared_array = Array('i', large_list)

# Use raw types
shared_value = Value('d', 0.0)  # Double
```

## Alternatives to Pickle
```python
import marshal  # Faster for simple data
import json     # For JSON-serializable data

# Custom serialization
class CustomObject:
    def __getstate__(self):
        # Return serializable state
        return {"data": self.data}

    def __setstate__(self, state):
        # Restore from state
        self.data = state["data"]
```

## Measuring Serialization Costs
```python
import cProfile
from multiprocessing import Queue

def send_large_data(q, data):
    q.put(data)

data = list(range(100000))
q = Queue()

cProfile.run('send_large_data(q, data)', 'profile.stats')
# Analyze profile.stats for pickle overhead
```

## Best Practices
- **Minimize Data Transfer**: Use shared memory when possible
- **Batch Operations**: Send fewer, larger messages
- **Simple Types**: Use basic types over complex objects
- **Compress Data**: For large transfers
- **Profile Performance**: Measure serialization costs

## Common Issues
- **Unpicklable Objects**: Some objects can't be pickled
- **Version Compatibility**: Pickle format changes
- **Security**: Never unpickle untrusted data
- **Performance**: Unexpected serialization costs

## Alternatives
- **Shared Memory**: For read-heavy data
- **Memory-Mapped Files**: For large datasets
- **Database**: For persistent shared data
- **Message Queues**: Redis, RabbitMQ for distributed systems

## Monitoring
```python
# Track serialization time
import time

class TimedQueue(Queue):
    def put(self, obj, block=True, timeout=None):
        start = time.time()
        result = super().put(obj, block, timeout)
        elapsed = time.time() - start
        print(f"Serialization took {elapsed:.4f}s")
        return result
```

## Optimization Checklist
- Profile serialization costs
- Use shared memory for large data
- Minimize inter-process communication
- Choose appropriate data structures
- Consider compression for large transfers
