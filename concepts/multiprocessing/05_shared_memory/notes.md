# Shared Memory in Multiprocessing

## Overview
Shared memory allows multiple processes to access the same data in memory, providing fast inter-process communication without serialization overhead. Python's multiprocessing module provides several shared memory mechanisms.

## Value Objects
```python
from multiprocessing import Process, Value
import time

def worker(shared_val):
    for _ in range(100):
        with shared_val.get_lock():
            shared_val.value += 1

shared_value = Value('i', 0)  # Integer, initial value 0

processes = [Process(target=worker, args=(shared_value,)) for _ in range(4)]
for p in processes: p.start()
for p in processes: p.join()

print(f"Final value: {shared_value.value}")  # Should be 400
```

## Array Objects
```python
from multiprocessing import Array

def modify_array(shared_arr):
    for i in range(len(shared_arr)):
        shared_arr[i] *= 2

shared_array = Array('i', [1, 2, 3, 4, 5])  # Integer array

p = Process(target=modify_array, args=(shared_array,))
p.start()
p.join()

print(list(shared_array))  # [2, 4, 6, 8, 10]
```

## Manager Objects
```python
from multiprocessing import Manager

def update_dict(shared_dict, key, value):
    shared_dict[key] = value

manager = Manager()
shared_dict = manager.dict()

processes = [Process(target=update_dict, args=(shared_dict, f"key{i}", i*10))
             for i in range(5)]

for p in processes: p.start()
for p in processes: p.join()

print(dict(shared_dict))  # {'key0': 0, 'key1': 10, ...}
```

## Shared Memory Types
- **Value**: Single value with type
- **Array**: Fixed-size array
- **Manager**: Proxy objects for complex data structures
- **RawArray**: Direct memory access (unsafe)

## Synchronization
```python
from multiprocessing import Lock

shared_data = Value('i', 0)
lock = Lock()

def safe_increment(val, lock):
    with lock:
        val.value += 1
```

## Performance Considerations
- **Speed**: Much faster than queues for simple data
- **Memory**: Shared memory is efficient
- **Synchronization**: Locks add overhead
- **Complexity**: Harder to debug race conditions

## Data Types
```python
# Supported ctypes
'i' : signed int
'I' : unsigned int
'l' : signed long
'L' : unsigned long
'f' : float
'd' : double
```

## Advanced Usage
```python
# Custom shared objects
class SharedCounter:
    def __init__(self):
        self.value = Value('i', 0)
        self.lock = Lock()

    def increment(self):
        with self.lock:
            self.value.value += 1

    def get(self):
        with self.lock:
            return self.value.value
```

## Limitations
- **Type Restrictions**: Limited to ctypes-compatible types
- **Size Fixed**: Arrays have fixed size
- **Inheritance**: Manager objects don't support all operations
- **Debugging**: Harder to debug shared memory issues

## Best Practices
- Use locks for synchronization
- Choose appropriate data types
- Handle process crashes gracefully
- Test thoroughly for race conditions
- Document shared memory usage
