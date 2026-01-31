"""
04 QUEUES — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise demonstrates specific multiprocessing 04_queues concepts
- Test your implementations after completion
"""


# Exercise 1: Producer-consumer with Queue
# TODO: Implement producer-consumer pattern using multiprocessing.Queue
def producer_consumer_queue():
    """Create producer and consumer processes using Queue"""
    from multiprocessing import Process, Queue
    import time
    
    def producer(q, items):
        # TODO: Iterate through items
        # TODO: Put each item in queue
        # TODO: Add small delay between items
        # TODO: Print progress
        pass
    
    def consumer(q):
        # TODO: Loop to get items from queue
        # TODO: Check for termination signal (None)
        # TODO: Process each item
        # TODO: Print progress
        pass
    
    # TODO: Create Queue
    # TODO: Define items to produce
    # TODO: Create producer and consumer processes
    # TODO: Start processes
    # TODO: Wait for producer to finish
    # TODO: Send termination signal to consumer
    # TODO: Wait for consumer to finish
    pass

# Exercise 2: Queue size and blocking behavior
# TODO: Demonstrate queue size limits and blocking operations
def queue_size_limits():
    """Show how queue size affects blocking behavior"""
    from multiprocessing import Process, Queue
    import time
    
    def fast_producer(q):
        # TODO: Put many items quickly
        # TODO: Show how queue fills up
        pass
    
    def slow_consumer(q):
        # TODO: Get items slowly
        # TODO: Show consumption rate
        pass
    
    # TODO: Create queue with size limit
    # TODO: Create producer and consumer processes
    # TODO: Observe blocking behavior
    pass
