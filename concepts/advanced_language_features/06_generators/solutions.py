# Generators Exercises Solutions

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes(limit):
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

for p in primes(10):
    print(p)  # 2 3 5 7