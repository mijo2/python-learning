# Multiprocessing Module Examples

from multiprocessing import Process
import time

def cpu_task(n):
    return sum(i * i for i in range(n))

processes = [Process(target=lambda: print(cpu_task(10**6))) for _ in range(4)]
start = time.time()
for p in processes: p.start()
for p in processes: p.join()
print(f"Time: {time.time() - start:.2f}s")  # Faster than threads