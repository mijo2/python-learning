# Generators Examples

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(5):
    print(num)  # 0 1 1 2 3

# Generator expression
squares = (x**2 for x in range(4))
print(list(squares))  # [0, 1, 4, 9]

# Infinite generator
def infinite_counter():
    n = 0
    while True:
        yield n
        n += 1

counter = infinite_counter()
print(next(counter))  # 0
print(next(counter))  # 1

# With send
def echo():
    while True:
        received = (yield)
        yield received

gen = echo()
next(gen)  # Prime
print(gen.send("Hello"))  # Hello
next(gen)
print(gen.send("World"))  # World