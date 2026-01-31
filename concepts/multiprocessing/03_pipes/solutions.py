"""
03 PIPES — SOLUTIONS
"""

from multiprocessing import Process, Pipe
import time

# Exercise 1: Basic pipe communication
def sender(conn):
    messages = ["Hello", "from", "child", "process"]
    for msg in messages:
        conn.send(msg)
        print(f"Sent: {msg}")
        time.sleep(0.1)
    conn.send(None)  # Signal end
    conn.close()

def receiver(conn):
    while True:
        msg = conn.recv()
        if msg is None:
            break
        print(f"Received: {msg}")
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()

    send_proc = Process(target=sender, args=(child_conn,))
    recv_proc = Process(target=receiver, args=(parent_conn,))

    send_proc.start()
    recv_proc.start()

    send_proc.join()
    recv_proc.join()
