"""
07 DEADLOCKS — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise demonstrates specific threading_synchronization 07_deadlocks concepts
- Test your implementations after completion
"""


# Exercise 1: Demonstrate deadlock scenario
# TODO: Create a scenario that causes deadlock
def demonstrate_deadlock():
    """Show how deadlocks can occur"""
    import threading
    import time
    
    lock1 = threading.Lock()
    lock2 = threading.Lock()
    
    def thread1():
        # TODO: Acquire locks in order that causes deadlock
        # TODO: Simulate work
        # TODO: Release locks
        pass
    
    def thread2():
        # TODO: Acquire locks in conflicting order
        # TODO: Simulate work
        # TODO: Release locks
        pass
    
    # TODO: Start threads and observe deadlock
    pass

# Exercise 2: Fix deadlock with proper lock ordering
# TODO: Fix the deadlock by acquiring locks in consistent order
def fix_deadlock():
    """Resolve deadlock with proper lock ordering"""
    # TODO: Modify lock acquisition order
    # TODO: Ensure deadlock-free execution
    pass
