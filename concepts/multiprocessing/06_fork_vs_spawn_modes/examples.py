def run():
    print("=== 06 Fork Vs Spawn Modes Examples ===\n")

    import multiprocessing as mp
    import os

    # Example 1: Check available start methods
    print("1. Available Start Methods:")
    methods = mp.get_all_start_methods()
    print(f"  Available: {methods}")

    current = mp.get_start_method()
    print(f"  Current: {current}")
    print()

    # Example 2: Demonstrate start method differences
    print("2. Start Method Differences:")

    def worker():
        print(f"  Worker PID: {os.getpid()}")
        print(f"  Parent PID: {os.getppid()}")
        print(f"  Start method used: {mp.get_start_method()}")

    for method in methods:
        print(f"\n  Testing {method}:")
        try:
            mp.set_start_method(method, force=True)
            p = mp.Process(target=worker)
            p.start()
            p.join()
        except RuntimeError as e:
            print(f"    {method} not supported: {e}")

    print()

    # Example 3: Context manager approach
    print("3. Using Context Manager:")

    def context_worker(name):
        print(f"  {name} - PID: {os.getpid()}")

    # Create different contexts
    contexts = {}
    for method in methods[:2]:  # Test first 2 methods
        try:
            contexts[method] = mp.get_context(method)
            print(f"  Created context for {method}")
        except ValueError:
            print(f"  {method} not available")

    # Use contexts
    for method, ctx in contexts.items():
        print(f"\n  Using {method} context:")
        p = ctx.Process(target=context_worker, args=(f"{method} process",))
        p.start()
        p.join()

    print()

    # Example 4: Performance comparison
    print("4. Performance Comparison:")

    def cpu_task(n):
        return sum(i*i for i in range(n))

    import time

    test_size = 50000

    for method in methods[:2]:  # Test available methods
        try:
            mp.set_start_method(method, force=True)

            start_time = time.time()

            with mp.Pool(processes=2) as pool:
                results = pool.map(cpu_task, [test_size, test_size])

            end_time = time.time()

            print(f"  {method}: {end_time - start_time:.3f}s, result: {results}")

        except (RuntimeError, ValueError) as e:
            print(f"  {method}: Not available ({e})")

if __name__ == "__main__":
    run()
