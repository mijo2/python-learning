# Generator Pipelines Exercises

# Exercise: Create a pipeline to filter and transform numbers

def numbers(n):
    for i in range(n):
        yield i

def filter_even(nums):
    # TODO: Yield even numbers
    pass

def multiply_by_2(nums):
    # TODO: Yield num * 2
    pass

# Uncomment to test
# pipeline = multiply_by_2(filter_even(numbers(10)))
# print(list(pipeline))  # [0, 4, 8, 12, 16]