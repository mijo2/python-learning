# Reference Counting Examples

import sys

# Basic ref counting
x = [1, 2, 3]
print("After x =", sys.getrefcount(x) - 1)  # Subtract 1 for the arg

y = x
print("After y = x", sys.getrefcount(x) - 1)

del y
print("After del y", sys.getrefcount(x) - 1)

# Circular reference
a = []
b = []
a.append(b)
b.append(a)
print("Circular refs:", sys.getrefcount(a) - 1)

# GC will handle cycles
import gc
gc.collect()
print("After GC")