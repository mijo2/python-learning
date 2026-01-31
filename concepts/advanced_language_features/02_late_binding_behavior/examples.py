# Late Binding Behavior Examples

# Problem
funcs = []
for i in range(3):
    funcs.append(lambda: i)

print("Problem:", [f() for f in funcs])  # [2, 2, 2]

# Solution 1: Default argument
funcs = []
for i in range(3):
    funcs.append(lambda x=i: x)

print("Solution 1:", [f() for f in funcs])  # [0, 1, 2]

# Solution 2: Partial
from functools import partial
funcs = [partial(lambda x: x, i) for i in range(3)]
print("Solution 2:", [f() for f in funcs])  # [0, 1, 2]