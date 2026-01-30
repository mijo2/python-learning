# Class Decorators

**Class decorators** work on classes, similar to function decorators but for entire classes. They can modify class behavior, add methods, or register classes.

## Basic Class Decorator

A class decorator takes a class and returns a modified class.

```python
def add_method(cls):
    cls.new_method = lambda self: "Added method"
    return cls

@add_method
class MyClass:
    pass

obj = MyClass()
print(obj.new_method())  # Added method
```

## How It Works

- `@add_method` is `MyClass = add_method(MyClass)`.
- The decorator returns the modified class.

## Advanced Example: Singleton

```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self, name):
        self.name = name

db1 = Database("main")
db2 = Database("main")
print(db1 is db2)  # True
```

## Uses

- Singletons
- Registration
- Adding class attributes/methods
- Validation

## Best Practices

- Return a class or callable.
- Use for cross-cutting concerns.
- Combine with metaclasses if needed.

Experiment with a class decorator that adds logging. This complements function decorators. Next, generators.