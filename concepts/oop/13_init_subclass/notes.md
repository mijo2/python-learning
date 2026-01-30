# Custom Class Creation Hooks (__init_subclass__)

Brilliant! Metaclasses gave you class-level control. For simpler subclass customization, use **`__init_subclass__`**, a method called when a class is subclassed. It's like `__init__` for classes—easier than metaclasses for many tasks.

Perfect for registering subclasses or setting defaults.

## What is __init_subclass__?

A class method called during subclass creation. Customize subclasses without metaclasses.

```python
class PluginBase:
    plugins = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)  # Call parent
        cls.plugins.append(cls)
        cls.name = kwargs.get('name', cls.__name__)

class MyPlugin(PluginBase, name='CustomPlugin'):
    pass

print(PluginBase.plugins)  # [<class '__main__.MyPlugin'>]
print(MyPlugin.name)       # CustomPlugin
```

Registers subclasses and sets attributes via kwargs.

## Why Use It?

1. **Simpler Than Metaclasses**: No need for custom `type`.
2. **Keyword Args**: Pass config to subclasses.
3. **Inheritance Aware**: Respects MRO with `super()`.
4. **Plugin Systems**: Auto-register subclasses.

## Advanced Example: Configurable Subclasses

```python
class Model:
    table_name = None

    def __init_subclass__(cls, table=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if table:
            cls.table_name = table
        else:
            cls.table_name = cls.__name__.lower()

class User(Model, table='users'):
    pass

class Product(Model):  # Defaults to 'product'
    pass

print(User.table_name)    # users
print(Product.table_name) # product
```

## Best Practices

- Use `super().__init_subclass__(**kwargs)` for chaining.
- Pass configs via keyword args.
- Combine with ABCs/protocols.

## Pitfalls

1. **Not for Instances**: Only called on subclassing, not instantiation.
2. **Order**: Called after metaclass, before `__init__`.
3. **No Return**: Modifies cls in place.

Create a base `Shape` class with `__init_subclass__` registering shapes by name. Subclass `Circle` and `Square`. This wraps up OOP—congrats on mastering classes!