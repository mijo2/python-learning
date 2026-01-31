# Context Managers Exercises

from contextlib import contextmanager

# Exercise: Create a context manager for changing directory

import os

@contextmanager
def change_dir(path):
    # TODO: Save current dir, change to path, yield, then restore
    pass

# Uncomment to test
# with change_dir('/tmp'):
#     print(os.getcwd())
# print(os.getcwd())  # Back to original