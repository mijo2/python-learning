# Custom Context Managers Exercises Solutions

from contextlib import contextmanager
import time

@contextmanager
def time_execution():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Elapsed: {end - start:.2f}s")

with time_execution():
    time.sleep(0.5)  # Elapsed: 0.50s