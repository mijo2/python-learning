# Context Managers Examples

from contextlib import contextmanager
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        self.end = time.time()
        print(f"Elapsed: {self.end - self.start:.2f}s")

with Timer():
    time.sleep(0.5)

# Using contextlib
@contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Elapsed: {end - start:.2f}s")

with timer():
    time.sleep(0.5)

# File example
with open('temp.txt', 'w') as f:
    f.write("Test")
# Closed automatically