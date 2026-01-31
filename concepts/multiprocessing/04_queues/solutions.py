"""
04 QUEUES — SOLUTIONS
"""

from multiprocessing import Process, Queue
import time

# Exercise 1: Basic queue operations
def producer(q, items):
    for item in items:
        q.put(item)
        print(f"Produced: {item}")
        time.sleep(0.1)

def consumer(q):
    while True:
        item = q.get()
        if item is None:  # Sentinel value
            break
        print(f"Consumed: {item}")
        time.sleep(0.2)

if __name__ == "__main__":
    q = Queue()
    items = ["item1", "item2", "item3"]

    prod = Process(target=producer, args=(q, items))
    cons = Process(target=consumer, args=(q,))

    prod.start()
    cons.start()

    prod.join()
    q.put(None)  # Signal end
    cons.join()
