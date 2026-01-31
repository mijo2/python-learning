"""
06 FORK VS SPAWN MODES — SOLUTIONS
"""

import multiprocessing as mp
import os

# Exercise 1: Check available start methods
def check_start_methods():
    methods = mp.get_all_start_methods()
    print(f"Available start methods: {methods}")

    current = mp.get_start_method()
    print(f"Current start method: {current}")

    return methods, current

# Exercise 2: Demonstrate start method differences
def worker():
    print(f"Worker process PID: {os.getpid()}")
    print(f"Parent process PID: {os.getppid()}")

if __name__ == "__main__":
    methods, current = check_start_methods()

    print("\nTesting different start methods:")
    for method in methods:
        try:
            print(f"\nTrying {method}:")
            mp.set_start_method(method, force=True)
            p = mp.Process(target=worker)
            p.start()
            p.join()
        except RuntimeError as e:
            print(f"  {method} not supported: {e}")
