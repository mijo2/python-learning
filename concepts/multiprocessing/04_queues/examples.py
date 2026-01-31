def run():
    print("=== 04 Queues Examples ===\n")

    from multiprocessing import Process, Queue
    import time

    # Example 1: Basic queue operations
    print("1. Basic Queue Operations:")
    q = Queue()

    # Put items in queue
    for i in range(5):
        q.put(f"Item {i}")
        print(f"  Put: Item {i}")

    # Get items from queue
    while not q.empty():
        item = q.get()
        print(f"  Got: {item}")

    print()

    # Example 2: Producer-consumer pattern
    print("2. Producer-Consumer Pattern:")

    def producer(q, items):
        for item in items:
            q.put(item)
            print(f"  Producer put: {item}")
            time.sleep(0.1)

    def consumer(q):
        while True:
            item = q.get()
            if item is None:  # Sentinel value
                break
            print(f"  Consumer got: {item}")
            time.sleep(0.2)

    items = ["Task A", "Task B", "Task C"]
    q = Queue()

    prod = Process(target=producer, args=(q, items))
    cons = Process(target=consumer, args=(q,))

    prod.start()
    cons.start()

    prod.join()
    q.put(None)  # Signal end
    cons.join()

    print("\n3. Queue Size and Status:")
    q = Queue(maxsize=3)

    print(f"  Initial size: {q.qsize()}")
    print(f"  Is empty: {q.empty()}")
    print(f"  Is full: {q.full()}")

    q.put("First")
    print(f"  After put - size: {q.qsize()}, empty: {q.empty()}, full: {q.full()}")

    q.put("Second")
    q.put("Third")
    print(f"  After 3 puts - size: {q.qsize()}, empty: {q.empty()}, full: {q.full()}")

if __name__ == "__main__":
    run()
