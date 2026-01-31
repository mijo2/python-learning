"""
05 SHARED MEMORY — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise demonstrates specific multiprocessing 05_shared_memory concepts
- Test your implementations after completion
"""


# Exercise 1: Shared counter with synchronization
# TODO: Create a counter that multiple processes can safely increment
def shared_memory_counter():
    """Demonstrate shared memory with proper synchronization"""
    from multiprocessing import Process, Value, Lock
    import time
    
    def increment_counter(shared_val, lock):
        # TODO: Use lock to safely increment
        # TODO: Perform multiple increments
        # TODO: Print progress
        pass
    
    # TODO: Create shared Value and Lock
    # TODO: Create multiple processes
    # TODO: Start processes and wait
    # TODO: Print final result
    pass

# Exercise 2: Shared array operations
# TODO: Manipulate shared arrays across multiple processes
def shared_array_operations():
    """Work with shared arrays"""
    from multiprocessing import Process, Array, Lock
    
    def modify_array(shared_arr, process_id, lock):
        # TODO: Use lock for synchronization
        # TODO: Modify array elements
        # TODO: Print changes
        pass
    
    # TODO: Create shared Array
    # TODO: Create processes to modify array
    # TODO: Start and wait for processes
    # TODO: Print final array state
    pass
