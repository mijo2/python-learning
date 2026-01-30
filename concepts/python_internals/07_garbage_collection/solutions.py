# Garbage Collection Exercises Solutions

import gc

a = []
b = []
a.append(b)
b.append(a)
print("Cycle created")
gc.collect()
print("Cycle collected")