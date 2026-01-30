# Multiple Inheritance and MRO (Method Resolution Order)

Great! Protocols gave you flexible interfaces. Now, let's tackle **multiple inheritance**, where a class inherits from multiple parents. This is powerful but tricky—Python uses **Method Resolution Order (MRO)** to decide which method to call when there's a conflict.

Imagine a `Smartphone` inheriting from `Phone` and `Computer`. Which `power_on()` method runs? MRO answers that!

## What is Multiple Inheritance?

A class can inherit from two or more base classes, combining their features.

```python
class Phone:
    def call(self):
        print("Calling...")

class Computer:
    def compute(self):
        print("Computing...")

class Smartphone(Phone, Computer):  # Multiple inheritance
    def browse(self):
        print("Browsing...")

phone = Smartphone()
phone.call()     # From Phone
phone.compute()  # From Computer
phone.browse()   # From Smartphone
```

## Method Resolution Order (MRO)

When methods conflict (same name in multiple parents), Python follows C3 linearization—a depth-first, left-to-right order with no duplicates.

- **Order**: Child → Parents (left to right) → Grandparents, etc.
- **Check MRO**: Use `Class.__mro__` or `Class.mro()`.

```python
class A:
    def method(self):
        print("A")

class B:
    def method(self):
        print("B")

class C(A, B):  # A before B
    pass

c = C()
c.method()  # Prints "A" (A is first)
print(C.__mro__)  # (C, A, B, object)
```

If `C(B, A)`, it would print "B" first.

## Why MRO Matters

1. **Predictability**: Know which method will be called.
2. **Diamond Problem**: Avoids ambiguity in complex hierarchies.
3. **Super() Calls**: `super()` follows MRO for cooperative inheritance.

## Cooperative Inheritance with super()

Use `super()` to call parent methods in order.

```python
class A:
    def __init__(self, name):
        self.name = name
        print("A init")

class B:
    def __init__(self, age):
        self.age = age
        print("B init")

class C(A, B):
    def __init__(self, name, age):
        super().__init__(name)  # Calls A.__init__
        super().__init__(age)   # Then B.__init__ via MRO
        print("C init")

c = C("Alice", 30)
# Output: A init, B init, C init
```

`super()` follows MRO: A then B.

## Best Practices

- **Keep It Simple**: Avoid deep multiple inheritance—use composition if possible.
- **Check MRO**: Always inspect `__mro__` for complex hierarchies.
- **Use super()**: For proper initialization chains.
- **Mixins**: Small, focused classes for reusable behavior.

## Pitfalls

1. **Diamond Problem**: In older languages, this caused issues—MRO solves it.
2. **Method Conflicts**: Unintended overriding—name methods carefully.
3. **Complexity**: Hard to debug—favor composition over inheritance.

Create classes `Flyer`, `Swimmer`, `Duck(Flyer, Swimmer)` with conflicting `move()` methods. Experiment with MRO and `super()`. This builds on ABCs and protocols for advanced design. You're mastering inheritance—next up, mixins!