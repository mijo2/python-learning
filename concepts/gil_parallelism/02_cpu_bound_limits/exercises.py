# CPU Bound Threading Limits Exercises

import threading
import time

def cpu_task(n):
    return sum(i for i in range(n))

# Exercise: Time single vs threaded

# TODO: Run single and with 2 threads, print times
# Uncomment
# start = time.time()
# cpu_task(10**7)
# print(f"Single: {time.time() - start:.2f}s")

# threads = [threading.Thread(target=cpu_task, args=(10**7,)) for _ in range(2)]
# start = time.time()
# for t in threads: t.start()
# for t in threads: t.join()
# print(f"Threaded: {time.time() - start:.2f}s")