# Attribute Lookup Chain in Python

## Overview
When you access an attribute on an object (`obj.attr`), Python follows a specific order to find the attribute. This is the attribute lookup chain.

## Lookup Order for `obj.attr`
1. **Data descriptors** on the class (descriptors that implement `__set__` or `__delete__`)
2. **Instance dictionary** (`obj.__dict__`)
3. **Non-data descriptors** on the class (descriptors that only implement `__get__`)
4. **Class dictionary** (`type(obj).__dict__`)
5. **Method Resolution Order (MRO)** - Check base classes in MRO order
6. **Raise AttributeError**

## For Class Attributes `Class.attr`
1. Class dictionary
2. MRO
3. Raise AttributeError

## Descriptors Take Precedence
- Data descriptors override instance attributes
- This is why `obj.x = 1` doesn't override a property

## `__getattribute__` and `__getattr__`
- `__getattribute__` is called for all attribute access
- `__getattr__` is called only if attribute not found
- Useful for custom lookup behavior

## Example
```python
class A:
    x = 1  # Class attribute

class B(A):
    pass

obj = B()
obj.x = 2  # Instance attribute
print(obj.x)  # 2 (instance overrides class)

# With descriptor
class Descriptor:
    def __get__(self, instance, owner):
        return "descriptor"

class C:
    attr = Descriptor()

c = C()
print(c.attr)  # descriptor (descriptor takes precedence)
c.__dict__['attr'] = 'instance'
print(c.attr)  # descriptor (data descriptor wins)
```

## Key Points
- Instance attributes hide class attributes
- Descriptors can override everything
- MRO affects inheritance