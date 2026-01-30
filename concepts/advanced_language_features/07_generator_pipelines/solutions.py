# Generator Pipelines Exercises Solutions

def numbers(n):
    for i in range(n):
        yield i

def filter_even(nums):
    for num in nums:
        if num % 2 == 0:
            yield num

def multiply_by_2(nums):
    for num in nums:
        yield num * 2

pipeline = multiply_by_2(filter_even(numbers(10)))
print(list(pipeline))  # [0, 4, 8, 12, 16]