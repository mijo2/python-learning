# Slots (__slots__) and Memory Optimization

Fantastic! Immutability protected your data. Now, optimize memory with **`__slots__`**, a class attribute that restricts instance attributes. This saves RAM by avoiding the dynamic `__dict__` per instance, ideal for memory-constrained apps or many objects.

Think of `__slots__` as declaring fixed fields—no extras allowed.

## What is __slots__?

A tuple/list of allowed attribute names. Prevents `__dict__` creation.

```python
class RegularClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlottedClass:
    __slots__ = ['x', 'y']  # Only these attributes allowed
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = SlottedClass(1, 2)
print(obj.x)  # 1
# obj.z = 3  # AttributeError: 'SlottedClass' object has no attribute 'z'
```

- **Memory Savings**: No per-instance dict—uses fixed slots.
- **Faster Access**: Direct attribute access.
- **Restrictions**: No dynamic attributes, no weakrefs by default.

## When to Use?

1. **Many Instances**: e.g., 10k+ objects.
2. **Known Attributes**: Fixed schema.
3. **Performance Critical**: Faster attribute access.

## Advanced Usage

1. **Inheritance**: Subclasses can add slots.
   ```python
   class Child(SlottedClass):
       __slots__ = ['z']
   ```

2. **Weakrefs**: Allow weak references.
   ```python
   __slots__ = ('x', 'y', '__weakref__')
   ```

3. **Descriptors**: Still work with slots.

## Best Practices

- Use for data-heavy classes (e.g., dataclasses with slots).
- Profile memory usage first.
- Avoid for classes needing dynamic attributes.

## Pitfalls

1. **No __dict__**: Can't add arbitrary attributes—breaks some libraries.
2. **Inheritance Complexity**: Slots in parents affect children.
3. **Pickling**: Works, but careful with evolution.

Add `__slots__` to a previous class and measure memory (use `sys.getsizeof`). Compare. This leads to metaclasses for advanced customization. You're optimizing like a champ!