# Type Hints Deep Dive Examples

from typing import Union, Optional, List

def greet(name: str) -> str:
    return f"Hello {name}"

def process(data: Union[str, int]) -> str:
    return str(data)

names: List[str] = ["Alice", "Bob"]
age: Optional[int] = None

print(greet("Alice"))
print(process(42))
print(names, age)