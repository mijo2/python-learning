def run():
    print("=== 05 Shared Memory Examples ===\n")

    from multiprocessing import Process, Value, Array, Lock
    import time

    # Example 1: Shared Value
    print("1. Shared Value:")

    def increment_value(shared_val):
        for _ in range(10):
            with shared_val.get_lock():
                shared_val.value += 1
                print(f"  Incremented to: {shared_val.value}")

    shared_value = Value('i', 0)  # Integer, initial value 0

    processes = [Process(target=increment_value, args=(shared_value,)) for _ in range(3)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f"  Final value: {shared_value.value}")
    print()

    # Example 2: Shared Array
    print("2. Shared Array:")

    def modify_array(shared_arr, process_id):
        for i in range(len(shared_arr)):
            with shared_arr.get_lock():
                shared_arr[i] += process_id
        print(f"  Process {process_id} modified array: {list(shared_arr)}")

    shared_array = Array('i', [1, 2, 3, 4, 5])  # Integer array

    processes = [Process(target=modify_array, args=(shared_array, i)) for i in range(1, 4)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f"  Final array: {list(shared_array)}")
    print()

    # Example 3: Shared Array of different types
    print("3. Shared Array of Different Types:")

    # Double array
    double_array = Array('d', [1.1, 2.2, 3.3])
    print(f"  Double array: {list(double_array)}")

    # Character array (fixed size)
    char_array = Array('c', b'hello')
    print(f"  Character array: {list(char_array)}")

    # Modify character array
    if len(char_array) > 0:
        char_array[0] = b'H'
    print(f"  Modified char array: {list(char_array)}")

    print()

    # Example 4: Synchronization with shared memory
    print("4. Synchronization with Shared Memory:")

    shared_counter = Value('i', 0)
    lock = Lock()

    def safe_increment(counter, lock, process_id):
        for _ in range(5):
            with lock:
                temp = counter.value
                time.sleep(0.01)  # Simulate work
                counter.value = temp + 1
                print(f"  Process {process_id}: {counter.value}")

    processes = [Process(target=safe_increment, args=(shared_counter, lock, i)) for i in range(3)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f"  Final synchronized counter: {shared_counter.value}")

if __name__ == "__main__":
    run()
