# Process Pools Examples

from multiprocessing import Pool
import time

def compute(x):
    time.sleep(0.1)  # Simulate work
    return x ** 2

if __name__ == '__main__':
    with Pool(4) as p:
        results = p.map(compute, range(10))
        print(results)

    # Async
    with Pool(4) as p:
        result = p.apply_async(compute, (5,))
        print(result.get())  # 25