# Custom Context Managers Exercises

from contextlib import contextmanager

# Exercise: Create a context manager that measures execution time

@contextmanager
def time_execution():
    # TODO: Record start time, yield, then print elapsed
    pass

# Uncomment to test
# with time_execution():
#     import time
#     time.sleep(0.5)  # Should print ~0.5s