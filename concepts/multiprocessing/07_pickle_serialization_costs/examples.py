def run():
    print("=== 07 Pickle Serialization Costs Examples ===\n")

    import pickle
    import time
    from multiprocessing import Process, Queue

    # Example 1: Measure serialization time
    print("1. Measuring Serialization Time:")

    def measure_serialization(data, description):
        # Serialize
        start = time.time()
        pickled = pickle.dumps(data)
        pickle_time = time.time() - start

        # Deserialize
        start = time.time()
        unpickled = pickle.loads(pickled)
        unpickle_time = time.time() - start

        size = len(pickled)

        print(f"  {description}:")
        print(f"    Size: {size} bytes")
        print(f"    Pickle time: {pickle_time:.6f}s")
        print(f"    Unpickle time: {unpickle_time:.6f}s")
        print(f"    Total time: {pickle_time + unpickle_time:.6f}s")

        return size, pickle_time, unpickle_time

    # Test different data types
    test_data = [
        ("Small dict", {"key": "value"}),
        ("Large dict", {"data": list(range(1000))}),
        ("Nested structure", {"users": [{"id": i, "data": list(range(10))} for i in range(100)]}),
        ("Simple list", list(range(1000))),
        ("String", "A" * 10000),
    ]

    for desc, data in test_data:
        measure_serialization(data, desc)
        print()

    # Example 2: Serialization in multiprocessing
    print("2. Serialization Overhead in Multiprocessing:")

    def worker(q, data):
        # Receive data (deserialization happens here)
        received = q.get()
        # Send result back (serialization happens here)
        q.put(f"Processed: {len(str(received))}")

    large_data = {"massive": list(range(50000))}

    q = Queue()

    start_time = time.time()

    p = Process(target=worker, args=(q, large_data))
    p.start()

    # Put data (serialization happens here)
    q.put(large_data)

    # Get result (deserialization happens here)
    result = q.get()

    p.join()

    total_time = time.time() - start_time

    print(f"  Multiprocessing with large data:")
    print(f"    Total time: {total_time:.4f}s")
    print(f"    Result: {result}")

    print()

    # Example 3: Comparing protocols
    print("3. Comparing Pickle Protocols:")

    data = {"complex": {"nested": {"data": list(range(100))}}}

    for protocol in range(pickle.HIGHEST_PROTOCOL + 1):
        start = time.time()
        pickled = pickle.dumps(data, protocol=protocol)
        pickle_time = time.time() - start

        size = len(pickled)

        print(f"  Protocol {protocol}: size={size}, time={pickle_time:.6f}s")

    print()

    # Example 4: Custom objects serialization
    print("4. Custom Objects Serialization:")

    class CustomObject:
        def __init__(self, value):
            self.value = value
            self.data = list(range(100))

        def __reduce__(self):
            # Custom reduction for efficient serialization
            return (self.__class__, (self.value,))

    obj = CustomObject(42)

    # Without custom __reduce__
    regular_size, _, _ = measure_serialization(obj, "Regular object")

    # The object has a __reduce__ method, so it will use that
    print(f"  Custom object size: {regular_size} bytes")

if __name__ == "__main__":
    run()
