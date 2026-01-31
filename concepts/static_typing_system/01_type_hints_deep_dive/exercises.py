# Type Hints Deep Dive Exercises

from typing import List, Optional

# Exercise: Add type hints to function

def sum_list(nums):  # TODO: Add hints for List[int] -> int
    return sum(nums)

# TODO: Add hints to variable
result = sum_list([1, 2, 3])  # Should be int

# Uncomment to test
# print(result)