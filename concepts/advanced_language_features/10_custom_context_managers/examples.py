# Custom Context Managers Examples

from contextlib import contextmanager, ExitStack

class Transaction:
    def __enter__(self):
        print("Starting transaction")
        return self
    
    def __exit__(self, *args):
        print("Committing transaction")

with Transaction():
    print("Doing work")

# Function-based
@contextmanager
def log_execution(func_name):
    print(f"Starting {func_name}")
    try:
        yield
    finally:
        print(f"Finished {func_name}")

with log_execution("my_func"):
    print("Executing")

# ExitStack for multiple
with ExitStack() as stack:
    stack.enter_context(open('file1.txt', 'w'))
    stack.enter_context(open('file2.txt', 'w'))
    print("Using multiple files")