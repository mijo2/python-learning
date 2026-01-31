# Multiprocessing Module Exercises

from multiprocessing import Process
import time

# Exercise: Run CPU task with processes

def cpu_task(n):
    return sum(i for i in range(n))

# TODO: Create 4 processes running cpu_task(10**7), time it
# Uncomment to test
# processes = [Process(target=cpu_task, args=(10**7,)) for _ in range(4)]
# start = time.time()
# for p in processes: p.start()
# for p in processes: p.join()
# print(f"Time: {time.time() - start:.2f}s")