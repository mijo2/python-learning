"""
05 WORKLOAD CLASSIFICATION — SOLUTIONS
"""

import time
import threading
import multiprocessing as mp

# Exercise 1: CPU-bound task
def cpu_intensive(n):
    return sum(i**2 for i in range(n))

# Exercise 2: IO-bound task
def io_intensive(duration):
    time.sleep(duration)
    return f"Slept for {duration}s"

# Exercise 3: Profile and classify
def profile_task(task_func, *args):
    start = time.time()
    result = task_func(*args)
    end = time.time()
    duration = end - start
    print(f"Task took {duration:.2f}s")
    return result

# Exercise 4: Test with threading
def test_threading():
    print("Testing IO-bound with threading:")
    threads = []
    for i in range(3):
        t = threading.Thread(target=lambda: profile_task(io_intensive, 1))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

# Exercise 5: Test with multiprocessing
def test_multiprocessing():
    print("Testing CPU-bound with multiprocessing:")
    with mp.Pool(processes=3) as pool:
        results = pool.map(cpu_intensive, [500000] * 3)
        for result in results:
            print(f"Result: {result}")

if __name__ == "__main__":
    print("Profiling tasks:")
    profile_task(cpu_intensive, 500000)
    profile_task(io_intensive, 1)

    print("\nTesting concurrency approaches:")
    test_threading()
    test_multiprocessing()
