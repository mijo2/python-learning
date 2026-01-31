"""
05 ASYNC CONTEXT MANAGERS — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise demonstrates specific async_programming 05_async_context_managers concepts
- Test your implementations after completion
"""


# Exercise 1: Create async context manager class
# TODO: Implement __aenter__ and __aexit__ methods
class AsyncDatabaseConnection:
    """Async context manager for database"""
    
    def __init__(self, connection_string):
        self.connection_string = connection_string
    
    async def __aenter__(self):
        # TODO: Simulate connection setup
        # TODO: Return connection object
        pass
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # TODO: Simulate connection cleanup
        pass

# Exercise 2: Use @asynccontextmanager decorator
# TODO: Create async context manager with decorator
from contextlib import asynccontextmanager

@asynccontextmanager
async def async_file_handler(filename, mode):
    # TODO: Simulate file opening
    # TODO: Yield file handle
    # TODO: Simulate file closing
    pass

# Exercise 3: Nested async context managers
# TODO: Use multiple async context managers together
async def nested_async_contexts():
    """Demonstrate nested async contexts"""
    # TODO: Use multiple async context managers
    # TODO: Show proper nesting and cleanup
    pass
