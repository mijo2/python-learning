# CPython vs PyPy Differences Examples

import sys
print("Python Implementation:", sys.implementation.name)
print("Version:", sys.version)

# Performance test
import time

def cpu_task():
    return sum(i**2 for i in range(10**6))

start = time.time()
result = cpu_task()
print(f"Time: {time.time() - start:.2f}s")
print("Result:", result)