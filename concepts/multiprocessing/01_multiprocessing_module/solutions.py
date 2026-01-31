# Multiprocessing Module Exercises Solutions

from multiprocessing import Process
import time

def cpu_task(n):
    return sum(i for i in range(n))

processes = [Process(target=cpu_task, args=(10**7,)) for _ in range(4)]
start = time.time()
for p in processes: p.start()
for p in processes: p.join()
print(f"Time: {time.time() - start:.2f}s")  # Parallel execution