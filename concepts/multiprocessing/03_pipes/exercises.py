"""
03 PIPES — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise demonstrates specific multiprocessing 03_pipes concepts
- Test your implementations after completion
"""


# Exercise 1: Basic pipe communication
# TODO: Create a pipe and send messages between parent and child processes
def basic_pipe_communication():
    """Demonstrate basic pipe usage between processes"""
    from multiprocessing import Process, Pipe
    import time
    
    def sender(conn):
        # TODO: Send greeting message
        # TODO: Send current time
        # TODO: Send list of numbers
        # TODO: Send termination signal
        # TODO: Close connection
        pass
    
    def receiver(conn):
        # TODO: Receive messages in loop
        # TODO: Handle different message types
        # TODO: Print received messages
        # TODO: Close connection when done
        pass
    
    # TODO: Create Pipe
    # TODO: Create sender and receiver processes
    # TODO: Start processes
    # TODO: Wait for completion
    pass

# Exercise 2: Bidirectional pipe communication
# TODO: Create pipes that allow communication in both directions
def bidirectional_pipe():
    """Show communication in both directions"""
    from multiprocessing import Process, Pipe
    
    def chat_process(conn, process_name):
        # TODO: Send introduction message
        # TODO: Receive and respond to messages
        # TODO: Handle conversation flow
        pass
    
    # TODO: Create two pipes for bidirectional communication
    # TODO: Create two processes that can chat
    # TODO: Start processes and observe conversation
    pass
