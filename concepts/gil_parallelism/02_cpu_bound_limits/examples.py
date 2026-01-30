# CPU Bound Threading Limits Examples

import threading
import time

def cpu_task():
    return sum(i**2 for i in range(10**6))

# Single-threaded
start = time.time()
result = cpu_task()
print(f"Single: {time.time() - start:.2f}s")

# Multi-threaded
threads = [threading.Thread(target=cpu_task) for _ in range(4)]
start = time.time()
for t in threads: t.start()
for t in threads: t.join()
print(f"Threaded: {time.time() - start:.2f}s")  # Likely similar or worse