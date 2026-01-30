# Process Pools Exercises Solutions

from multiprocessing import Pool

def double(x):
    return x * 2

if __name__ == '__main__':
    with Pool(2) as p:
        results = p.map(double, [1, 2, 3, 4])
        print(results)  # [2, 4, 6, 8]