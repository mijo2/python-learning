# Late Binding Behavior

**Late binding** in closures and lambdas can cause unexpected behavior due to variable lookup at execution time.

## The Issue

In loops, closures capture variables by reference, not value.

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)

print([f() for f in funcs])  # [2, 2, 2] not [0, 1, 2]
```

All lambdas reference the same `i`, which is 2 after the loop.

## Solutions

1. Use default argument to capture current value.

```python
funcs = []
for i in range(3):
    funcs.append(lambda x=i: x)

print([f() for f in funcs])  # [0, 1, 2]
```

2. Use partial from functools.

```python
from functools import partial

funcs = [partial(lambda x: x, i) for i in range(3)]
print([f() for f in funcs])  # [0, 1, 2]
```

## Why It Happens

- Variables are looked up in enclosing scopes at call time.
- Closures hold references, not copies.

Be aware in loops and list comprehensions. This is key for closures. Next, function decorators.