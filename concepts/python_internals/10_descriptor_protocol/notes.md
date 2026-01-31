# Descriptor Protocol in Python

## Overview
The descriptor protocol allows objects to customize attribute access. Descriptors are the mechanism behind properties, methods, and other attribute behaviors.

## Descriptor Methods
- `__get__(self, instance, owner)` - Called to get the attribute
- `__set__(self, instance, value)` - Called to set the attribute
- `__delete__(self, instance)` - Called to delete the attribute

## Types of Descriptors
- **Data Descriptor**: Implements `__set__` and/or `__delete__`
- **Non-Data Descriptor**: Only implements `__get__`

## Method Resolution Order
When accessing `obj.attr`:
1. Data descriptors (on class)
2. Instance dictionary
3. Non-data descriptors (on class)
4. Class dictionary
5. MRO

## Built-in Descriptors
- `property`
- `staticmethod`
- `classmethod`
- `functools.cached_property`

## Creating Custom Descriptors
```python
class MyDescriptor:
    def __init__(self, initial_value=None):
        self.value = initial_value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.value

    def __set__(self, instance, value):
        self.value = value
```

## Use Cases
- Validation
- Computed attributes
- Lazy loading
- Type checking