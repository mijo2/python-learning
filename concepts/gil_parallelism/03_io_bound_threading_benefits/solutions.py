"""
03 IO BOUND THREADING BENEFITS — SOLUTIONS
"""

import threading
import time
import requests

# Exercise 1: Simulate IO-bound task
def io_task(task_id, duration=1):
    print(f"Starting task {task_id}")
    time.sleep(duration)  # Simulate IO operation
    print(f"Completed task {task_id}")
    return f"Result {task_id}"

# Exercise 2: Sequential execution
def sequential_execution():
    start_time = time.time()
    results = []
    for i in range(3):
        results.append(io_task(i, 1))
    end_time = time.time()
    print(f"Sequential time: {end_time - start_time:.2f}s")
    return results

# Exercise 3: Concurrent execution with threads
def concurrent_execution():
    start_time = time.time()
    threads = []
    results = []

    def thread_worker(task_id):
        result = io_task(task_id, 1)
        results.append(result)

    for i in range(3):
        t = threading.Thread(target=thread_worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()
    print(f"Concurrent time: {end_time - start_time:.2f}s")
    return results

if __name__ == "__main__":
    print("Sequential execution:")
    sequential_execution()

    print("\nConcurrent execution:")
    concurrent_execution()
