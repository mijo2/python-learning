# GIL Behavior Exercises Solutions

import threading
import time

def cpu_task(n):
    return sum(i for i in range(n))

# Single-threaded
start = time.time()
result = cpu_task(10**7)
print(f"Single: {time.time() - start:.2f}s")

# Multi-threaded (GIL prevents parallelism)
threads = [threading.Thread(target=lambda: cpu_task(10**7)) for _ in range(4)]
start = time.time()
for t in threads: t.start()
for t in threads: t.join()
print(f"Multi: {time.time() - start:.2f}s")  # Similar time due to GIL