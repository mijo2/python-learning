# Garbage Collection Examples

import gc

# Create a cycle
a = []
b = []
a.append(b)
b.append(a)

print("Before GC:", len(gc.get_objects()))  # Many objects
gc.collect()
print("After GC")  # Cycle collected

# Disable GC
gc.disable()
print("GC disabled")

gc.enable()
print("GC enabled")