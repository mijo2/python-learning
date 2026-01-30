# Parameterized Decorators Examples

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello {name}")

greet("Alice")

class Logged:
    def __init__(self, level="INFO"):
        self.level = level
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"[{self.level}] Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper

@Logged("DEBUG")
def add(a, b):
    return a + b

print(add(1, 2))