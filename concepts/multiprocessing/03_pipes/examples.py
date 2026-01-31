def run():
    print("=== 03 Pipes Examples ===\n")

    from multiprocessing import Process, Pipe
    import time

    # Example 1: Basic pipe communication
    print("1. Basic Pipe Communication:")

    def sender(conn):
        messages = ["Hello", "from", "child", "process"]
        for msg in messages:
            conn.send(msg)
            print(f"  Sent: {msg}")
            time.sleep(0.1)
        conn.close()

    def receiver(conn):
        while conn.poll():  # Check if data available
            msg = conn.recv()
            print(f"  Received: {msg}")
        conn.close()

    parent_conn, child_conn = Pipe()

    send_proc = Process(target=sender, args=(child_conn,))
    recv_proc = Process(target=receiver, args=(parent_conn,))

    send_proc.start()
    recv_proc.start()

    send_proc.join()
    recv_proc.join()

    print()

    # Example 2: Bidirectional communication
    print("2. Bidirectional Communication:")

    def bidirectional_worker(conn, name):
        # Send greeting
        conn.send(f"Hello from {name}")

        # Receive response
        response = conn.recv()
        print(f"  {name} received: {response}")

        # Send farewell
        conn.send(f"Goodbye from {name}")
        conn.close()

    parent_conn1, child_conn1 = Pipe()
    parent_conn2, child_conn2 = Pipe()

    proc1 = Process(target=bidirectional_worker, args=(child_conn1, "Process A"))
    proc2 = Process(target=bidirectional_worker, args=(child_conn2, "Process B"))

    proc1.start()
    proc2.start()

    # Parent communicates with both
    msg1 = parent_conn1.recv()
    print(f"  Parent received from A: {msg1}")
    parent_conn1.send("Response to A")

    msg2 = parent_conn2.recv()
    print(f"  Parent received from B: {msg2}")
    parent_conn2.send("Response to B")

    # Receive farewells
    farewell1 = parent_conn1.recv()
    farewell2 = parent_conn2.recv()
    print(f"  Farewell from A: {farewell1}")
    print(f"  Farewell from B: {farewell2}")

    proc1.join()
    proc2.join()

    print()

    # Example 3: Pipe with timeout
    print("3. Pipe with Timeout:")
    parent_conn, child_conn = Pipe()

    def slow_sender(conn):
        time.sleep(2)
        conn.send("Delayed message")
        conn.close()

    proc = Process(target=slow_sender, args=(child_conn,))
    proc.start()

    # Try to receive with timeout
    if parent_conn.poll(timeout=1):
        msg = parent_conn.recv()
        print(f"  Received: {msg}")
    else:
        print("  No message received within timeout")

    proc.join()
    parent_conn.close()

if __name__ == "__main__":
    run()
