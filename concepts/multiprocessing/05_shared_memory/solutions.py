"""
05 SHARED MEMORY — SOLUTIONS
"""

from multiprocessing import Process, Value, Array, Lock
import time

# Exercise 1: Shared counter
def increment_counter(counter, lock):
    for _ in range(100):
        with lock:
            counter.value += 1

if __name__ == "__main__":
    counter = Value('i', 0)  # Integer, initial value 0
    lock = Lock()

    processes = [Process(target=increment_counter, args=(counter, lock)) for _ in range(4)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f"Final counter value: {counter.value}")  # Should be 400
