# Object Model

Python's **object model** is everything-is-an-object philosophy. Classes, functions, even types are objects. This enables dynamic behavior and introspection.

## Everything is an Object

- **Classes**: Instances of `type`.
- **Instances**: Have `__class__` pointing to their class.
- **Functions**: Callable objects with attributes.

```python
class MyClass:
    pass

obj = MyClass()
print(type(MyClass))  # <class 'type'>
print(obj.__class__)  # <class '__main__.MyClass'>
```

## Attributes and Methods

- **Instance Attributes**: Stored in `__dict__`.
- **Class Attributes**: Shared, in class `__dict__`.
- **Methods**: Functions bound to instances.

## Identity, Type, Value

Objects have identity (`id()`), type (`type()`), and value.

## Dynamic Nature

Add attributes at runtime, monkey-patch, etc.

Experiment with `dir()`, `hasattr()`, `getattr()`. This model powers Python's flexibility. Next, memory layout.