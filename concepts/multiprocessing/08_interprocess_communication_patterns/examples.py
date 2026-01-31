def run():
    print("=== 08 Interprocess Communication Patterns Examples ===\n")

    from multiprocessing import Process, Queue, Value, Lock
    import time
    import random

    # Example 1: Producer-consumer with multiple producers/consumers
    print("1. Producer-Consumer with Multiple Processes:")

    def producer(q, producer_id, num_items):
        for i in range(num_items):
            item = f"Item {producer_id}-{i}"
            q.put(item)
            print(f"  Producer {producer_id} produced: {item}")
            time.sleep(random.uniform(0.1, 0.3))

    def consumer(q, consumer_id):
        items_processed = 0
        while True:
            item = q.get()
            if item is None:  # Sentinel value
                q.put(None)  # Re-signal for other consumers
                break
            print(f"  Consumer {consumer_id} processed: {item}")
            items_processed += 1
            time.sleep(random.uniform(0.2, 0.4))

        print(f"  Consumer {consumer_id} processed {items_processed} items")

    q = Queue()

    # Start 2 producers and 3 consumers
    producers = [Process(target=producer, args=(q, i, 3)) for i in range(2)]
    consumers = [Process(target=consumer, args=(q, i)) for i in range(3)]

    print("  Starting producers and consumers...")
    for p in producers + consumers:
        p.start()

    # Wait for producers to finish
    for p in producers:
        p.join()

    # Signal consumers to stop
    for _ in consumers:
        q.put(None)

    # Wait for consumers
    for p in consumers:
        p.join()

    print()

    # Example 2: Work sharing with load balancing
    print("2. Load Balancing with Shared Counter:")

    shared_counter = Value('i', 0)
    lock = Lock()
    results_q = Queue()

    def worker(worker_id, tasks_q, results_q, counter, lock):
        processed = 0
        while True:
            task = tasks_q.get()
            if task is None:
                tasks_q.put(None)  # Re-signal
                break

            # Simulate processing time
            time.sleep(random.uniform(0.1, 0.5))

            with lock:
                counter.value += 1
                task_id = counter.value

            result = f"Worker {worker_id} processed task '{task}' -> Result {task_id}"
            results_q.put(result)
            processed += 1

        print(f"  Worker {worker_id} processed {processed} tasks")

    # Create task and result queues
    tasks_q = Queue()

    # Add tasks
    tasks = [f"Task {i}" for i in range(10)]
    for task in tasks:
        tasks_q.put(task)

    # Start workers
    num_workers = 3
    workers = [Process(target=worker, args=(i, tasks_q, results_q, shared_counter, lock))
               for i in range(num_workers)]

    for w in workers:
        w.start()

    # Signal workers to stop
    for _ in workers:
        tasks_q.put(None)

    # Collect results
    results = []
    for _ in range(len(tasks)):
        result = results_q.get()
        results.append(result)

    for w in workers:
        w.join()

    print("  Results:")
    for result in sorted(results):
        print(f"    {result}")

    print(f"  Total tasks processed: {len(results)}")

if __name__ == "__main__":
    run()
