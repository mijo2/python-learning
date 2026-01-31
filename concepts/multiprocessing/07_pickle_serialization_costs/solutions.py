"""
07 PICKLE SERIALIZATION COSTS — SOLUTIONS
"""

import pickle
import time
from multiprocessing import Process, Queue

# Exercise 1: Measure serialization time
def measure_serialization(data):
    start = time.time()
    pickled = pickle.dumps(data)
    pickle_time = time.time() - start

    start = time.time()
    unpickled = pickle.loads(pickled)
    unpickle_time = time.time() - start

    return len(pickled), pickle_time, unpickle_time

# Exercise 2: Compare data sizes
def compare_data_sizes():
    small_data = {"key": "value"}
    large_data = {"data": list(range(10000))}

    small_size, small_pickle, small_unpickle = measure_serialization(small_data)
    large_size, large_pickle, large_unpickle = measure_serialization(large_data)

    print(f"Small data: size={small_size}, pickle={small_pickle:.4f}s, unpickle={small_unpickle:.4f}s")
    print(f"Large data: size={large_size}, pickle={large_pickle:.4f}s, unpickle={large_unpickle:.4f}s")

if __name__ == "__main__":
    compare_data_sizes()
