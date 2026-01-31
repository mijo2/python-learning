"""
03 IO BOUND THREADING BENEFITS — EXERCISES

Instructions:
- Learn why threading helps with IO-bound tasks despite the GIL
- Implement concurrent IO operations and measure performance improvements
"""

import threading
import time
import requests

# Exercise 1: Simulate IO-bound operations
# Create a function that simulates network requests or file operations
# TODO: Implement a function that simulates an IO-bound task (like downloading a file)
def io_bound_task(task_id, duration=1.0):
    """
    Simulate an IO-bound task (like a network request).
    In real code, this might be: requests.get(url) or file operations
    """
    # TODO: Print start message with task_id
    # TODO: Use time.sleep() to simulate IO wait time
    # TODO: Print completion message
    # TODO: Return a result string
    pass

# Exercise 2: Sequential vs Concurrent execution
# Compare the performance of sequential vs threaded IO operations
# TODO: Implement sequential execution of multiple IO tasks
def sequential_execution(num_tasks=3):
    """
    Execute IO tasks one after another (sequential).
    This simulates how a single-threaded program handles multiple IO operations.
    """
    start_time = time.time()
    results = []

    # TODO: Loop through num_tasks
    # TODO: Call io_bound_task for each task
    # TODO: Collect results
    # TODO: Calculate and return total time

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Sequential execution took {total_time:.2f} seconds")
    return results, total_time

# Exercise 3: Concurrent execution with threading
# Use threading to execute IO tasks concurrently
# TODO: Implement concurrent execution using threading
def concurrent_execution(num_tasks=3):
    """
    Execute IO tasks concurrently using threads.
    This shows how threading improves IO-bound workloads.
    """
    start_time = time.time()
    threads = []
    results = []

    # TODO: Create a thread-safe way to collect results (hint: use a lock)
    # TODO: Create and start threads for each task
    # TODO: Wait for all threads to complete
    # TODO: Calculate and return total time

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Concurrent execution took {total_time:.2f} seconds")
    return results, total_time

# Exercise 4: Compare performance and demonstrate GIL behavior
# TODO: Create a function that compares sequential vs concurrent performance
def compare_performance():
    """
    Demonstrate the performance difference between sequential and concurrent IO.
    This shows why threading helps with IO-bound tasks despite the GIL.
    """
    num_tasks = 5

    print("Comparing IO-bound task performance:")
    print("=" * 40)

    # Sequential
    print("Sequential execution:")
    seq_results, seq_time = sequential_execution(num_tasks)

    # Concurrent
    print("\nConcurrent execution (with threading):")
    conc_results, conc_time = concurrent_execution(num_tasks)

    # Analysis
    speedup = seq_time / conc_time if conc_time > 0 else 0
    print(".2f"
    # Test code (uncomment after implementation)
    # if __name__ == "__main__":
    #     compare_performance()
