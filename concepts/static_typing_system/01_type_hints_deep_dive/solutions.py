# Type Hints Deep Dive Exercises Solutions

from typing import List

def sum_list(nums: List[int]) -> int:
    return sum(nums)

result: int = sum_list([1, 2, 3])
print(result)