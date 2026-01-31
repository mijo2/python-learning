# Inspect Module

## Overview
The `inspect` module provides functions for introspecting live objects, getting source code, and examining the runtime environment. It's essential for debugging, testing, and metaprogramming.

## Getting Function Information
```python
import inspect

def example_function(a, b=10, *args, **kwargs):
    """Example function with various parameters."""
    return a + b

# Get function signature
sig = inspect.signature(example_function)
print(sig)  # (a, b=10, *args, **kwargs)

# Get parameters
params = sig.parameters
print(params['a'].default)  # <class 'inspect._empty'>
print(params['b'].default)  # 10
```

## Source Code Inspection
```python
# Get source code
source = inspect.getsource(example_function)
print(source)

# Get source lines with line numbers
lines, lineno = inspect.getsourcelines(example_function)
print(f"Function starts at line {lineno}")
```

## Object Type Checking
```python
class MyClass:
    def method(self):
        pass

obj = MyClass()

print(inspect.isclass(MyClass))      # True
print(inspect.ismethod(obj.method))  # True
print(inspect.isfunction(example_function))  # True
print(inspect.iscoroutinefunction(async_func))  # True
```

## Frame Inspection
```python
def trace_function():
    frame = inspect.currentframe()
    caller_frame = frame.f_back

    print(f"Current function: {frame.f_code.co_name}")
    print(f"Caller function: {caller_frame.f_code.co_name}")
    print(f"Local variables: {frame.f_locals}")
```

## Class and Method Inspection
```python
# Get class members
members = inspect.getmembers(MyClass)
methods = [name for name, obj in members if inspect.ismethod(obj)]

# Get method resolution order
print(inspect.getmro(MyClass))

# Check if method is inherited
print(inspect.getattr_static(obj, 'method'))
```

## Module Inspection
```python
import mymodule

# Get all functions in module
functions = [name for name, obj in inspect.getmembers(mymodule)
             if inspect.isfunction(obj)]

# Get module file location
print(inspect.getfile(mymodule))
```

## Live Object Introspection
```python
# Get instance attributes
attrs = inspect.getattr_static(obj, 'attribute_name')

# Check if attribute exists
print(hasattr(obj, 'attr'))  # Using hasattr
print(inspect.getattr_static(obj, 'attr', None))  # Using inspect
```

## Best Practices
- Use for debugging and development tools
- Be careful with performance in production code
- Handle exceptions when source code is unavailable
- Respect privacy when inspecting objects
- Use appropriate inspection functions for different object types
