# Weak References

## Overview
Weak references allow you to reference objects without preventing their garbage collection. They are useful for implementing caches, observers, and other patterns where you want to track objects without owning them.

## Basic Weak References
```python
import weakref

class ExpensiveObject:
    def __init__(self, name):
        self.name = name

obj = ExpensiveObject("test")
weak_ref = weakref.ref(obj)

# Access the object
print(weak_ref())  # <ExpensiveObject object>

# Delete the strong reference
del obj

# Object is garbage collected
print(weak_ref())  # None
```

## WeakKeyDictionary
```python
from weakref import WeakKeyDictionary

class Observer:
    def __init__(self):
        self.subjects = WeakKeyDictionary()

    def add_subject(self, subject):
        self.subjects[subject] = True

    def notify_all(self):
        for subject in self.subjects:
            subject.update()

# Subjects can be garbage collected without explicit removal
```

## WeakValueDictionary
```python
from weakref import WeakValueDictionary

cache = WeakValueDictionary()

def get_expensive_data(key):
    if key in cache:
        return cache[key]

    data = ExpensiveComputation(key)
    cache[key] = data
    return data

# Cached objects are automatically removed when no longer referenced
```

## WeakSet
```python
from weakref import WeakSet

active_connections = WeakSet()

class Connection:
    def __init__(self):
        active_connections.add(self)

    def close(self):
        active_connections.discard(self)

# Connections are automatically removed from the set when garbage collected
```

## Callbacks for Weak References
```python
def cleanup_callback(wr):
    print("Object was garbage collected")

obj = ExpensiveObject("test")
weak_ref = weakref.ref(obj, cleanup_callback)

del obj  # Triggers callback
```

## Weak Methods and Functions
```python
from weakref import WeakMethod

class MyClass:
    def method(self):
        return "method called"

obj = MyClass()
weak_method = WeakMethod(obj.method)

# Access the method
bound_method = weak_method()
if bound_method:
    result = bound_method()
```

## Best Practices
- Use weak references to avoid circular references
- Implement cleanup callbacks when needed
- Choose appropriate weak collection type
- Be prepared for None when dereferencing
- Use weak references in caching scenarios
