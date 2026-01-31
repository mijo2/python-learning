"""
MULTIPROCESSING SUBMULTIPROCESSING — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise shows what needs to be implemented
- Test your implementations after completion
"""

# Exercise 1: Create a basic process
# TODO: Use multiprocessing.Process to create and start a child process
def basic_process_creation():
    """Create and run a simple child process"""
    import multiprocessing as mp
    import os

    def worker():
        # TODO: Print process ID and parent PID
        # TODO: Do some simple work
        pass

    # TODO: Create Process object
    # TODO: Start the process
    # TODO: Wait for process to complete
    pass

# Exercise 2: Process with arguments
# TODO: Pass arguments to a child process
def process_with_arguments():
    """Create process that receives arguments"""
    import multiprocessing as mp

    def worker(name, count):
        # TODO: Print the name and count parameters
        # TODO: Loop count times printing iteration
        pass

    # TODO: Create process with args
    # TODO: Start and join process
    pass

# Exercise 3: Multiple processes
# TODO: Create and manage multiple concurrent processes
def multiple_processes():
    """Run multiple processes simultaneously"""
    import multiprocessing as mp
    import time

    def worker(worker_id, duration):
        # TODO: Print worker starting with ID
        # TODO: Sleep for specified duration
        # TODO: Print worker finished
        pass

    # TODO: Create list of processes with different durations
    # TODO: Start all processes
    # TODO: Wait for all to complete
    pass

# Exercise 4: Process information
# TODO: Examine process properties and information
def process_information():
    """Display information about current process"""
    import multiprocessing as mp
    import os

    # TODO: Print current process name
    # TODO: Print current process PID
    # TODO: Print parent process PID
    # TODO: Print number of CPU cores
    pass

# Test code (uncomment after implementation)
# if __name__ == "__main__":
#     print("=== Basic Process Creation ===")
#     basic_process_creation()
#
#     print("\n=== Process with Arguments ===")
#     process_with_arguments()
#
#     print("\n=== Multiple Processes ===")
#     multiple_processes()
#
#     print("\n=== Process Information ===")
#     process_information()
