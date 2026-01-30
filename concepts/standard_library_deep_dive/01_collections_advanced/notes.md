# Collections Advanced Types

The `collections` module offers powerful data structures beyond built-ins. Master these for efficient Python code.

## Key Types

1. **namedtuple**: Immutable, named fields.
   ```python
   from collections import namedtuple
   Point = namedtuple('Point', ['x', 'y'])
   p = Point(1, 2)
   print(p.x)  # 1
   ```

2. **deque**: Double-ended queue for fast appends/pops.
   ```python
   from collections import deque
   dq = deque([1, 2, 3])
   dq.appendleft(0)  # [0, 1, 2, 3]
   dq.pop()  # 3
   ```

3. **Counter**: Count hashable items.
   ```python
   from collections import Counter
   c = Counter('hello')
   print(c)  # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
   ```

4. **OrderedDict**: Dict with insertion order (Python 3.7+ dicts preserve order).
   ```python
   from collections import OrderedDict
   od = OrderedDict()
   od['a'] = 1
   od['b'] = 2
   ```

5. **defaultdict**: Dict with default values.
   ```python
   from collections import defaultdict
   dd = defaultdict(list)
   dd['a'].append(1)  # No KeyError
   ```

## Why Use Collections?

- **Performance**: Optimized for specific use cases.
- **Convenience**: Less code than custom implementations.
- **Readability**: Intent is clear.

Experiment with each type. Replace dicts/lists with collections where fitting. This deepens standard library knowledge!