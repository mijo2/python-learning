# Generator Pipelines Examples

from itertools import takewhile

def lines(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()

def words(lines_gen):
    for line in lines_gen:
        for word in line.split():
            yield word

def uppercase(words_gen):
    for word in words_gen:
        yield word.upper()

# Pipeline: lines -> words -> uppercase
pipeline = uppercase(words(["hello world", "foo bar"]))
print(list(pipeline))  # ['HELLO', 'WORLD', 'FOO', 'BAR']

# Fibonacci pipeline
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def squares(nums):
    for n in nums:
        yield n ** 2

fib_squares = takewhile(lambda x: x < 100, squares(fibonacci()))
print(list(fib_squares))  # [0, 1, 1, 4, 9, 25, 64]