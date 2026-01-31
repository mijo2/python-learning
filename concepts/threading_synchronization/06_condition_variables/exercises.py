"""
06 CONDITION VARIABLES — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise demonstrates specific threading_synchronization 06_condition_variables concepts
- Test your implementations after completion
"""


# Exercise 1: Basic condition variable usage
# TODO: Use condition variables for thread synchronization
def basic_condition_variable():
    """Demonstrate condition variable for producer-consumer"""
    import threading
    import queue
    
    condition = threading.Condition()
    queue = []
    max_size = 5
    
    def producer():
        # TODO: Produce items
        # TODO: Use condition.wait() when queue full
        # TODO: Use condition.notify() when item added
        pass
    
    def consumer():
        # TODO: Consume items
        # TODO: Use condition.wait() when queue empty
        # TODO: Use condition.notify() when item removed
        pass
    
    # TODO: Start producer and consumer threads
    pass

# Exercise 2: Multiple consumers with condition
# TODO: Handle multiple consumers with proper synchronization
def multiple_consumers_condition():
    """Multiple consumers using condition variables"""
    # TODO: Create shared buffer
    # TODO: Create condition variable
    # TODO: Create one producer, multiple consumers
    # TODO: Ensure proper synchronization
    pass
