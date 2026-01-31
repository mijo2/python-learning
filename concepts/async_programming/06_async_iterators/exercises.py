"""
06 ASYNC ITERATORS — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise demonstrates specific async_programming 06_async_iterators concepts
- Test your implementations after completion
"""


# Exercise 1: Create async iterator class
# TODO: Implement async iterator with __aiter__ and __anext__
class AsyncCounter:
    """Async iterator that counts"""
    
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
    
    def __aiter__(self):
        # TODO: Return self
        pass
    
    async def __anext__(self):
        # TODO: Check if limit reached
        # TODO: Raise StopAsyncIteration if done
        # TODO: Increment counter
        # TODO: Return current value
        pass

# Exercise 2: Create async generator
# TODO: Use async generator syntax
async def async_fibonacci(n):
    """Async generator for fibonacci numbers"""
    a, b = 0, 1
    for _ in range(n):
        # TODO: Yield current value
        # TODO: Update a, b
        pass

# Exercise 3: Use async iteration
# TODO: Consume async iterators
async def consume_async_iterators():
    """Demonstrate async iteration"""
    # TODO: Use async for loop
    # TODO: Collect results
    pass
