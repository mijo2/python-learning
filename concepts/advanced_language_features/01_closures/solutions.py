# Closures Exercises Solutions

def make_adder(n):
    def adder(x):
        return x + n
    return adder

add_ten = make_adder(10)
print(add_ten(5))  # 15