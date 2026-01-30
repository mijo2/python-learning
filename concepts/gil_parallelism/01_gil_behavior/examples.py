# GIL Behavior Examples

import threading
import time

def cpu_bound():
    return sum(i * i for i in range(10**6))

def io_bound():
    time.sleep(1)  # Simulates I/O

# CPU-bound with threads (GIL limits)
threads = [threading.Thread(target=cpu_bound) for _ in range(4)]
start = time.time()
for t in threads: t.start()
for t in threads: t.join()
print(f"CPU-bound time: {time.time() - start:.2f}s")

# I/O-bound with threads (GIL released)
threads = [threading.Thread(target=io_bound) for _ in range(4)]
start = time.time()
for t in threads: t.start()
for t in threads: t.join()
print(f"I/O-bound time: {time.time() - start:.2f}s")