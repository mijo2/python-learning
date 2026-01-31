"""
01 ITERATOR PROTOCOL — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise shows what needs to be implemented
- Test your implementations after completion
"""


# Exercise 1: Create a custom iterator class
# TODO: Implement __iter__ and __next__ methods
class CountdownIterator:
    """Iterator that counts down from n to 0"""

    def __init__(self, n):
        # TODO: Store starting number
        pass

    def __iter__(self):
        # TODO: Return self
        pass

    def __next__(self):
        # TODO: Check if counting is done
        # TODO: Raise StopIteration when finished
        # TODO: Return current number and decrement
        pass

# Exercise 2: Create an infinite iterator
# TODO: Implement an iterator that never stops
class FibonacciIterator:
    """Infinite iterator for Fibonacci sequence"""

    def __init__(self):
        # TODO: Initialize first two Fibonacci numbers
        pass

    def __iter__(self):
        # TODO: Return self
        pass

    def __next__(self):
        # TODO: Calculate next Fibonacci number
        # TODO: Update state for next iteration
        # TODO: Return current number
        pass

# Exercise 3: Use built-in iterators
# TODO: Demonstrate iter() and next() functions
def manual_iteration_demo():
    """Manually iterate through a list using iter() and next()"""
    # TODO: Create a list
    # TODO: Get iterator using iter()
    # TODO: Use next() to get elements
    # TODO: Handle StopIteration
    pass
