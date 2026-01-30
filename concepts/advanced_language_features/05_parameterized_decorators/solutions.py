# Parameterized Decorators Exercises Solutions

import random

def retry_on_failure(max_retries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries:
                        raise e
                    print(f"Attempt {attempt + 1} failed, retrying...")
        return wrapper
    return decorator

@retry_on_failure(2)
def risky_func():
    if random.choice([True, False]):
        raise ValueError("Random failure")
    return "Success"

print(risky_func())