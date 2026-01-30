# Closures Examples

def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
print(add_five(3))  # 8

def make_multiplier(factor):
    return lambda x: x * factor

double = make_multiplier(2)
print(double(10))  # 20