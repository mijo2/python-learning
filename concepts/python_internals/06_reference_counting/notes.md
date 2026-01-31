# Reference Counting

**Reference counting** is Python's primary memory management technique, tracking how many references point to an object.

## How It Works

Each object has a reference count. When it reaches zero, the object is deallocated.

```python
import sys

x = [1, 2, 3]  # ref count = 1
y = x           # ref count = 2
del y           # ref count = 1
del x           # ref count = 0, deallocated
```

## sys.getrefcount

Get the current reference count.

```python
import sys

a = []
print(sys.getrefcount(a))  # 2 (one for a, one for getrefcount arg)
```

## Cycles

Reference counting can't handle circular references. That's why Python has garbage collection.

## Manual Management

Use `del` to decrease count, but usually automatic.

## Pitfalls

- Circular references leak memory until GC runs.
- C extensions may not follow ref counting.

Use for understanding memory. Next, garbage collection.