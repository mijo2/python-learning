# GIL Behavior Exercises

import threading
import time

# Exercise: Compare single-threaded vs. multi-threaded CPU task

def cpu_task(n):
    return sum(i for i in range(n))

# TODO: Run cpu_task(10**7) single-threaded and with 4 threads, time both
# Uncomment and test
# start = time.time()
# result = cpu_task(10**7)
# print(f"Single: {time.time() - start:.2f}s")

# threads = [threading.Thread(target=cpu_task, args=(10**7,)) for _ in range(4)]
# start = time.time()
# for t in threads: t.start()
# for t in threads: t.join()
# print(f"Multi: {time.time() - start:.2f}s")  # Should be similar or slower