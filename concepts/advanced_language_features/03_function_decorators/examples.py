# Function Decorators Examples

from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f}s")
        return result
    return wrapper

@timer
def slow_func():
    import time
    time.sleep(0.1)
    return "Done"

print(slow_func())

# Multiple decorators
def upper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@upper
@timer
def greet(name):
    return f"Hello {name}"

print(greet("Bob"))