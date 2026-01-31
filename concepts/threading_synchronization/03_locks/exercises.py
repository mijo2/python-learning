"""
03 LOCKS — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise demonstrates specific threading_synchronization 03_locks concepts
- Test your implementations after completion
"""


# Exercise 1: Shared counter without synchronization (shows race condition)
# TODO: Create a counter that demonstrates race conditions
def unsafe_shared_counter():
    """Demonstrate race conditions with shared state"""
    import threading
    import time
    
    counter = 0
    
    def increment():
        nonlocal counter
        for _ in range(100):
            current = counter
            time.sleep(0.001)  # Simulate work
            counter = current + 1
    
    # TODO: Create multiple threads
    # TODO: Start threads and wait
    # TODO: Return final counter (will be wrong)
    return counter

# Exercise 2: Shared counter with Lock (proper synchronization)
# TODO: Fix the race condition using threading.Lock
def safe_shared_counter():
    """Use Lock to synchronize access to shared state"""
    import threading
    import time
    
    counter = 0
    lock = threading.Lock()
    
    def increment():
        nonlocal counter
        for _ in range(100):
            # TODO: Acquire lock
            # TODO: Read and update counter
            # TODO: Release lock
            pass
    
    # TODO: Create threads
    # TODO: Start and join threads
    # TODO: Return correct final counter
    return counter

# Exercise 3: Bank account with thread-safe operations
# TODO: Create a BankAccount class with synchronized deposit/withdraw
class BankAccount:
    """Thread-safe bank account"""
    
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        # TODO: Add lock for synchronization
    
    def deposit(self, amount):
        # TODO: Acquire lock
        # TODO: Update balance
        # TODO: Release lock
        pass
    
    def withdraw(self, amount):
        # TODO: Acquire lock
        # TODO: Check sufficient funds
        # TODO: Update balance if possible
        # TODO: Release lock
        # TODO: Return success status
        pass
    
    def get_balance(self):
        # TODO: Acquire lock
        # TODO: Return balance
        # TODO: Release lock
        pass
