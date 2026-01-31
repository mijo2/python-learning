# Process Pools Exercises

from multiprocessing import Pool

def double(x):
    return x * 2

# Exercise: Use Pool to double numbers in parallel

# TODO: Create pool with 2 processes, map double to [1,2,3,4]
# Uncomment
# if __name__ == '__main__':
#     with Pool(2) as p:
#         results = p.map(double, [1, 2, 3, 4])
#         print(results)