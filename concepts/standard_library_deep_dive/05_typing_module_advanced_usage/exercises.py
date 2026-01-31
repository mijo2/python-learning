"""
05 TYPING MODULE ADVANCED USAGE — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise shows what needs to be implemented
- Test your implementations after completion
"""


# Exercise 1: Context manager usage
# TODO: Use contextlib for resource management
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    """Simple context manager"""
    # TODO: Setup code (print acquisition)
    # TODO: Yield resource
    # TODO: Cleanup code (print release)
    pass

# Exercise 2: Weak references demonstration
# TODO: Show weak reference usage and cleanup
import weakref

def weak_reference_demo():
    """Demonstrate weak references"""
    # TODO: Create object
    # TODO: Create weak reference
    # TODO: Delete strong reference
    # TODO: Show weak reference behavior
    pass

# Exercise 3: Inspect module usage
# TODO: Use inspect to examine live objects
import inspect

def inspect_demo():
    """Use inspect module"""
    # TODO: Define function
    # TODO: Use inspect to get signature
    # TODO: Use inspect to get source
    # TODO: Check function properties
    pass
