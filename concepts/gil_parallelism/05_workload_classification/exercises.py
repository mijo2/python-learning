"""
05 WORKLOAD CLASSIFICATION — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise shows what needs to be implemented
- Test your implementations after completion
"""


# Exercise 1: CPU-bound task identification
# TODO: Identify if a task is CPU-bound or IO-bound
def identify_task_type():
    """Analyze different tasks and classify them"""
    # TODO: Create CPU-intensive task (mathematical computation)
    # TODO: Create IO-intensive task (simulated file/network operations)
    # TODO: Time both tasks
    # TODO: Classify based on results
    pass

# Exercise 2: Demonstrate GIL impact
# TODO: Show how GIL affects multithreaded CPU-bound tasks
def gil_impact_demo():
    """Compare single-threaded vs multithreaded CPU tasks"""
    # TODO: Create CPU-intensive function
    # TODO: Run single-threaded
    # TODO: Run multithreaded
    # TODO: Compare performance (should be similar due to GIL)
    pass

# Exercise 3: IO-bound threading benefits
# TODO: Show threading benefits for IO-bound tasks
def io_threading_benefits():
    """Demonstrate threading advantages for IO operations"""
    # TODO: Create IO-intensive tasks (simulated delays)
    # TODO: Run sequentially
    # TODO: Run with threading
    # TODO: Show performance improvement
    pass
