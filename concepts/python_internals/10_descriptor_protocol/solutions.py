"""
DESCRIPTOR PROTOCOL — SOLUTIONS
"""

# Exercise 1: Validated descriptor
class ValidatedDescriptor:
    def __init__(self, validator=None):
        self.validator = validator
        self.data = {}

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(id(instance), None)

    def __set__(self, instance, value):
        if self.validator and not self.validator(value):
            raise ValueError("Invalid value")
        self.data[id(instance)] = value

def is_positive(x):
    return x > 0

class Product:
    price = ValidatedDescriptor(is_positive)

p = Product()
p.price = 100
print("Ex1: p.price =", p.price)

try:
    p.price = -5
except ValueError as e:
    print("Ex1: Error:", e)

# Exercise 2: Lazy property
class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __get__(self, instance, owner):
        if instance is None:
            return self
        key = id(instance)
        if key not in self.cache:
            self.cache[key] = self.func(instance)
        return self.cache[key]

class Data:
    @LazyProperty
    def expensive_calc(self):
        print("Computing...")
        return 42

d = Data()
print("Ex2: First access:", d.expensive_calc)
print("Ex2: Second access:", d.expensive_calc)

# Exercise 3: Property for computed attribute
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

c = Circle(5)
print("Ex3: c.area =", c.area)
c._radius = 10
print("Ex3: c.area =", c.area)