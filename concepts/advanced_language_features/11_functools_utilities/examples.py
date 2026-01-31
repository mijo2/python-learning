# functools Utilities Examples

from functools import partial, lru_cache, reduce

# partial
def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(double(5))  # 10

# lru_cache
@lru_cache
def expensive(n):
    print(f"Computing {n}")
    return n * n

print(expensive(5))  # Computing 5
print(expensive(5))  # Cached

# reduce
nums = [1, 2, 3, 4]
sum_all = reduce(lambda x, y: x + y, nums, 0)
print(sum_all)  # 10

# total_ordering
from functools import total_ordering

@total_ordering
class Number:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value < other.value

n1 = Number(1)
n2 = Number(2)
print(n1 < n2)  # True
print(n1 <= n2) # True (auto-generated)