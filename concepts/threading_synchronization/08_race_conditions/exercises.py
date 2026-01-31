"""
08 RACE CONDITIONS — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise demonstrates specific threading_synchronization 08_race_conditions concepts
- Test your implementations after completion
"""


# Exercise 1: Demonstrate race condition
# TODO: Create a scenario that shows race conditions
def demonstrate_race_condition():
    """Show race condition in shared counter"""
    import threading
    import time
    
    counter = 0
    
    def increment():
        nonlocal counter
        for _ in range(1000):
            current = counter
            time.sleep(0.0001)  # Small delay exposes race
            counter = current + 1
    
    # TODO: Create multiple threads
    # TODO: Start threads and wait
    # TODO: Show incorrect final result
    return counter

# Exercise 2: Fix race condition with synchronization
# TODO: Use proper synchronization to fix race condition
def fix_race_condition():
    """Fix race condition with Lock"""
    # TODO: Add lock to prevent race condition
    # TODO: Ensure correct final result
    pass
