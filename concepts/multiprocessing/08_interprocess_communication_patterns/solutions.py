"""
08 INTERPROCESS COMMUNICATION PATTERNS — SOLUTIONS
"""

from multiprocessing import Process, Queue
import time
import random

# Exercise 1: Producer-consumer with queue
def producer(q, producer_id, num_items):
    for i in range(num_items):
        item = f"Item {producer_id}-{i}"
        q.put(item)
        print(f"Producer {producer_id} produced: {item}")
        time.sleep(random.uniform(0.1, 0.3))

def consumer(q, consumer_id):
    while True:
        item = q.get()
        if item is None:  # Sentinel value
            q.put(None)  # Re-signal for other consumers
            break
        print(f"Consumer {consumer_id} consumed: {item}")
        time.sleep(random.uniform(0.2, 0.4))

if __name__ == "__main__":
    q = Queue()

    # Start producers
    producers = [Process(target=producer, args=(q, i, 3)) for i in range(2)]

    # Start consumers
    consumers = [Process(target=consumer, args=(q, i)) for i in range(2)]

    for p in producers + consumers:
        p.start()

    for p in producers:
        p.join()

    # Signal consumers to stop
    for _ in consumers:
        q.put(None)

    for p in consumers:
        p.join()
