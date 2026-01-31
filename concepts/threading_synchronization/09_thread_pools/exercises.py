"""
09 THREAD POOLS — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise demonstrates specific threading_synchronization 09_thread_pools concepts
- Test your implementations after completion
"""


# Exercise 1: Basic thread pool usage
# TODO: Use ThreadPoolExecutor for concurrent tasks
def basic_thread_pool():
    """Demonstrate ThreadPoolExecutor usage"""
    from concurrent.futures import ThreadPoolExecutor
    import time
    
    def worker(task_id):
        # TODO: Simulate work
        # TODO: Return result
        pass
    
    # TODO: Create ThreadPoolExecutor
    # TODO: Submit tasks
    # TODO: Collect results
    pass

# Exercise 2: Handle exceptions in thread pool
# TODO: Properly handle exceptions from thread pool tasks
def thread_pool_exceptions():
    """Handle exceptions in thread pool"""
    from concurrent.futures import ThreadPoolExecutor, as_completed
    
    def risky_task(task_id):
        # TODO: Create task that may raise exception
        pass
    
    # TODO: Submit tasks that may fail
    # TODO: Handle exceptions properly
    pass
