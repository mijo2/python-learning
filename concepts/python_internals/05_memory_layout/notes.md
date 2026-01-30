# Memory Layout

Understanding **memory layout** helps optimize Python programs. Objects have overhead, and layouts differ by type.

## Object Header

Every object has a header with type pointer, refcount, etc.

## Instance Layout

- **__dict__**: Dictionary for attributes (hash table).
- **__slots__**: Fixed slots for memory efficiency.

## Container Layouts

- **Lists**: Dynamic arrays.
- **Dicts**: Hash tables.
- **Tuples**: Fixed-size arrays.

## Memory Management

- **Heap Allocation**: Objects on heap.
- **Garbage Collection**: Reference counting + cyclic GC.

Use `sys.getsizeof()` to measure. Optimize with `__slots__`, namedtuples. This knowledge aids performance tuning. Next, reference counting.