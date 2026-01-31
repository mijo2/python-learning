# Garbage Collection

Python uses **garbage collection (GC)** to handle memory deallocation, especially for cyclic references that reference counting can't resolve.

## Reference Counting Limitations

Reference counting fails on cycles: objects referencing each other.

```python
a = []
b = []
a.append(b)
b.append(a)  # Cycle: a -> b -> a
# del a, b  # Ref counts don't go to 0
```

## How GC Works

Python's GC is generational, using mark-and-sweep for cycles.

- **Generations**: 0 (young), 1, 2 (old).
- **Thresholds**: Objects promoted when surviving collections.
- **Automatic**: Runs in background, can be manual with `gc.collect()`.

## gc Module

```python
import gc

print(gc.get_stats())  # Collection stats
gc.collect()           # Force collection
gc.disable()           # Turn off GC
```

## Best Practices

- Avoid cycles where possible.
- Use weakrefs for caches.
- Monitor with `gc` for leaks.

## Pitfalls

- GC pauses can affect performance.
- Circular imports can cause issues.

Experiment with cycles and `gc.collect()`. This completes memory management. Next, mutability rules.