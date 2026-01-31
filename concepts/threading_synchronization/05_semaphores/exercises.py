"""
05 SEMAPHORES — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise demonstrates specific threading_synchronization 05_semaphores concepts
- Test your implementations after completion
"""


# Exercise 1: Basic semaphore for resource limiting
# TODO: Use semaphore to limit concurrent access to a resource
def semaphore_resource_limit():
    """Limit concurrent access using semaphore"""
    import threading
    import time
    
    semaphore = threading.Semaphore(3)  # Allow 3 concurrent
    
    def access_resource(thread_id):
        # TODO: Acquire semaphore
        # TODO: Simulate resource access
        # TODO: Release semaphore
        pass
    
    # TODO: Create multiple threads
    # TODO: Start threads and observe limiting
    pass

# Exercise 2: Producer-consumer with semaphore
# TODO: Use semaphores for producer-consumer synchronization
def semaphore_producer_consumer():
    """Producer-consumer using semaphores"""
    import threading
    import queue
    import time
    
    # TODO: Create queue
    # TODO: Create semaphores for empty/full slots
    # TODO: Create mutex for queue access
    
    def producer():
        # TODO: Produce items
        # TODO: Use semaphores correctly
        pass
    
    def consumer():
        # TODO: Consume items
        # TODO: Use semaphores correctly
        pass
    
    # TODO: Start producer and consumer threads
    pass
