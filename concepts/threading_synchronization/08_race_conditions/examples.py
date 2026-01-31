
def run():
    print("=== 08 RACE CONDITIONS Examples ===
")

    import threading
    import time

    # Example 1: Basic thread creation
    print("1. Basic Thread Creation:")
    print("   def worker(name):")
    print("       print(f'Worker {name} running')")
    print()
    print("   t = threading.Thread(target=worker, args=('A',))")
    print("   t.start()")
    print("   t.join()")

    print()

    # Example 2: Thread synchronization
    print("2. Thread Synchronization:")
    print("   lock = threading.Lock()")
    print("   with lock:")
    print("       shared_data.append(item)")

    print()

    # Example 3: Producer-consumer pattern
    print("3. Producer-Consumer Pattern:")
    print("   queue = Queue()")
    print("   # Producer thread puts items")
    print("   # Consumer thread gets items")

if __name__ == "__main__":
    run()
