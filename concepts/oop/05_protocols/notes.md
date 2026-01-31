# Interfaces via Protocols (typing.Protocol)

Fantastic progress! You've mastered abstract base classes for enforcing interfaces through inheritance. Now, let's explore **protocols**, a more flexible way to define interfaces using structural typing. Protocols are like "duck typing" on steroids—they check if an object has the right methods/attributes, regardless of inheritance.

Think of protocols as informal contracts: "If you quack like a duck and walk like a duck, you're a duck." No need to inherit from `Duck`—just behave like one!

## What Are Protocols?

Protocols are defined in `typing.Protocol` and use abstract methods to specify expected behavior. They're checked at static analysis time (e.g., with mypy) or runtime via `isinstance`.

```python
from typing import Protocol

class Speakable(Protocol):
    def speak(self) -> str:  # No implementation needed
        ...

class Dog:
    def speak(self) -> str:
        return "Woof!"

class Car:
    def speak(self) -> str:
        return "Vroom!"

def make_sound(obj: Speakable) -> str:
    return obj.speak()

dog = Dog()
car = Car()
print(make_sound(dog))  # Woof!
print(make_sound(car))  # Vroom!
```

`Dog` and `Car` don't inherit from anything—they just implement `speak()`. The protocol ensures type safety.

## Why Protocols Over ABCs?

1. **Flexibility**: No inheritance required—works with existing classes.
2. **Structural Typing**: Focus on behavior, not hierarchy.
3. **Runtime Checking**: Use `isinstance(obj, Protocol)` for dynamic checks.
4. **Better Composition**: Mix protocols without diamond inheritance issues.

## Protocol Features

1. **Simple Protocol**:
   ```python
   class Drawable(Protocol):
       def draw(self) -> None:
           ...
   ```

2. **With Properties**:
   ```python
   class HasName(Protocol):
       @property
       def name(self) -> str:
           ...
   ```

3. **Generic Protocols**:
   ```python
   from typing import TypeVar, Protocol

   T = TypeVar('T')

   class Container(Protocol[T]):
       def __getitem__(self, key) -> T:
           ...
   ```

4. **Runtime Registration**: Like ABCs, you can register classes.

## Real-World Example: File-Like Objects

Many libraries accept "file-like" objects. A protocol can define this:

```python
class FileLike(Protocol):
    def read(self, size: int = -1) -> str:
        ...
    def write(self, data: str) -> int:
        ...

def process_file(f: FileLike):
    data = f.read()
    # Process...
```

Now, any object with `read` and `write` methods works, even custom ones.

## Best Practices

- Use protocols for interfaces that span multiple classes.
- Combine with ABCs when inheritance makes sense.
- Always type hint with protocols for better tooling.
- Keep protocols simple—focus on essential methods.

## Pitfalls

1. **No Enforcement**: Unlike ABCs, protocols don't prevent instantiation of incomplete classes.
2. **Runtime Overhead**: `isinstance` checks can be slow for complex protocols.
3. **Confusion**: Duck typing might hide errors until runtime.

Create a `Movable` protocol with `move(dx, dy)` method, then implement it in `Point` and `Robot` classes. Test with a function that accepts `Movable`. This complements ABCs and prepares for multiple inheritance. Keep exploring—you're becoming a protocol pro!