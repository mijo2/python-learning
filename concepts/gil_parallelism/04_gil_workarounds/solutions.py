"""
04 GIL WORKAROUNDS — SOLUTIONS
"""

import multiprocessing as mp
import threading
import time

# Exercise 1: CPU-bound task
def cpu_task(n):
    return sum(i * i for i in range(n))

# Exercise 2: Threading approach (limited by GIL)
def threading_approach():
    start_time = time.time()

    threads = []
    results = []

    def thread_worker(n):
        result = cpu_task(n)
        results.append(result)

    for _ in range(4):
        t = threading.Thread(target=thread_worker, args=(1000000,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()
    print(f"Threading time: {end_time - start_time:.2f}s")
    return results

# Exercise 3: Multiprocessing approach
def multiprocessing_approach():
    start_time = time.time()

    with mp.Pool(processes=4) as pool:
        results = pool.map(cpu_task, [1000000] * 4)

    end_time = time.time()
    print(f"Multiprocessing time: {end_time - start_time:.2f}s")
    return results

if __name__ == "__main__":
    print("Threading approach:")
    threading_approach()

    print("\nMultiprocessing approach:")
    multiprocessing_approach()
