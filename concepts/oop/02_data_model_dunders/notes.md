# Data Model and Dunder Methods

Hello again, Python learner! Now that you have a grasp of basic classes, instances, methods, and attributes, let's dive into Python's **data model**. This is where Python gets really powerful and "magical." The data model is a set of protocols that define how objects behave in various situations—like how they're printed, compared, or used in collections. At the heart of this are **dunder methods** (short for "double underscore" methods, like `__str__`), which allow you to customize your objects' behavior.

Think of dunder methods as hooks that Python calls automatically when certain operations are performed on your objects. They're like special powers you can give your classes to make them more intuitive and integrated with Python's ecosystem.

## Why the Data Model Matters

1. **Customization**: Make your objects behave like built-in types (e.g., strings, lists).
2. **Consistency**: Follow Python's conventions for better readability and usability.
3. **Powerful Abstractions**: Enable advanced features like custom containers or callable objects.
4. **Debugging Aid**: Better representations help with logging and development.

By mastering dunder methods, you'll write more Pythonic code and understand why built-ins work the way they do.

## Core Dunder Methods: `__str__` and `__repr__`

These two are among the most common and important. They control how your object is represented as a string.

- **`__str__`**: For "user-friendly" output. Called by `str(obj)` or `print(obj)`. Should be readable and concise.
- **`__repr__`**: For "developer-friendly" output. Called by `repr(obj)` or in the REPL. Should be unambiguous, ideally recreatable code.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"{self.name} ({self.breed})"  # Friendly for users

    def __repr__(self):
        return f"Dog(name='{self.name}', breed='{self.breed}')"  # Precise for devs

my_dog = Dog("Buddy", "Golden Retriever")
print(str(my_dog))   # Buddy (Golden Retriever)
print(repr(my_dog))  # Dog(name='Buddy', breed='Golden Retriever')
```

**Tip**: If `__str__` is not defined, Python falls back to `__repr__`. Always implement `__repr__` first—it's more fundamental.

## Equality and Hashing: `__eq__` and `__hash__`

These control how objects are compared and used in sets/dicts. Objects that compare equal should have the same hash.

- **`__eq__`**: Defines equality (`==`). Return `NotImplemented` if types don't match.
- **`__hash__`**: Returns an integer hash. Immutable objects should be hashable.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __eq__(self, other):
        if not isinstance(other, Dog):
            return NotImplemented
        return self.name == other.name and self.breed == other.breed

    def __hash__(self):
        return hash((self.name, self.breed))

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Buddy", "Golden Retriever")
dog3 = Dog("Max", "Bulldog")

print(dog1 == dog2)  # True (same name and breed)
print(dog1 == dog3)  # False
print(hash(dog1) == hash(dog2))  # True (same hash for equal objects)
```

**Pitfall**: If you define `__eq__`, also define `__hash__` unless the class is mutable (in which case, set `__hash__ = None`).

## Other Essential Dunder Methods

1. **`__len__`**: For `len(obj)`. Return the "length" of your object.
   ```python
   def __len__(self):
       return len(self.items)  # If your class has an items list
   ```

2. **`__getitem__` and `__setitem__`**: For indexing (`obj[key]`) and assignment (`obj[key] = value`).
   ```python
   def __getitem__(self, key):
       return self.data[key]
   def __setitem__(self, key, value):
       self.data[key] = value
   ```

3. **`__iter__`**: For iteration (`for item in obj`). Return an iterator.
   ```python
   def __iter__(self):
       return iter(self.items)
   ```

4. **`__call__`**: Makes the object callable like a function.
   ```python
   def __call__(self, x):
       return x * 2  # Now you can do obj(5) -> 10
   ```

## Best Practices

- **Don't Overdo It**: Only implement dunder methods that make sense for your class.
- **Consistency**: Follow Python conventions (e.g., `__len__` should return an int).
- **Testing**: Always test your custom methods thoroughly.
- **Inheritance**: If subclassing, call `super()` in dunder methods if needed.

## Common Mistakes

1. **Forgetting `NotImplemented`**: In `__eq__`, return this for unsupported types.
2. **Mutable Hashing**: Don't hash mutable objects—use `__hash__ = None`.
3. **Ignoring Fallbacks**: Python has defaults, but they're often not ideal.

Experiment by adding these methods to your `Book` class from the previous lesson. For example, make books comparable by title. This will deepen your understanding of how objects interact in Python. Next, we'll explore operator overloading—stay tuned!