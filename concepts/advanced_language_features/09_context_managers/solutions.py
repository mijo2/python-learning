# Context Managers Exercises Solutions

from contextlib import contextmanager
import os

@contextmanager
def change_dir(path):
    original = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(original)

with change_dir('/tmp'):
    print(os.getcwd())
print(os.getcwd())  # Back to original