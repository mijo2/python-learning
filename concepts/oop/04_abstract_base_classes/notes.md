# Abstract Base Classes (ABC)

Excellent work so far! You've built custom classes with dunder methods and operator overloading. Now, let's explore **Abstract Base Classes (ABCs)**, a way to define blueprints or interfaces that ensure certain methods are implemented in subclasses. Think of ABCs as contracts: "If you inherit from me, you must provide these features."

ABCs promote clean, structured code by enforcing interfaces without dictating implementation details.

## What Are Abstract Base Classes?

- **Abstract**: Not meant to be instantiated directly.
- **Base Class**: Parent class for inheritance.
- **Interface Enforcement**: Subclasses must implement abstract methods.

ABCs are defined using the `abc` module. They help with polymorphism and type checking.

## Why Use ABCs?

1. **Enforce Interfaces**: Guarantee subclasses implement required methods.
2. **Polymorphism**: Write code that works with any subclass.
3. **Type Hints**: Better static type checking (e.g., with mypy).
4. **Design Clarity**: Separate "what" from "how" in your code.

## Basic ABC Example

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        """Abstract method: must be implemented by subclasses."""
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# dog = Dog()
# print(dog.speak())  # Woof!
# animal = Animal()  # TypeError: Can't instantiate abstract class
```

- `@abstractmethod`: Decorator marking methods as required.
- Subclasses must override all abstract methods, or they're abstract too.
- Abstract classes can have concrete methods too.

## Advanced ABC Features

1. **Concrete Methods in ABCs**:
   ```python
   class Animal(ABC):
       @abstractmethod
       def speak(self):
           pass
       
       def describe(self):  # Concrete method
           return f"I am an animal that says {self.speak()}"
   ```

2. **Abstract Properties**:
   ```python
   @property
   @abstractmethod
   def name(self):
       pass
   ```

3. **Registering Classes**: Use `ABC.register()` to make existing classes "inherit" without subclassing.
   ```python
   class Duck:
       def speak(self):
           return "Quack!"
   
   Animal.register(Duck)  # Now Duck is considered an Animal
   ```

## Real-World Use: Shape Hierarchy

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
```

Now, any function expecting a `Shape` will work with `Circle` or `Rectangle`.

## Best Practices

- Use ABCs for "is-a" relationships (e.g., Dog is-an Animal).
- Keep abstract methods minimal—focus on the interface.
- Combine with protocols (next lesson) for more flexibility.
- Document abstract methods clearly.

## Common Pitfalls

1. **Trying to Instantiate**: Abstract classes can't be created directly.
2. **Missing Implementations**: Subclasses must implement all abstract methods.
3. **Over-Abstraction**: Don't make everything abstract—balance with concrete code.

Create an ABC for `Vehicle` with abstract `drive()` method, then implement `Car` and `Bike`. This reinforces inheritance and prepares for multiple inheritance. You're building a strong OOP foundation—keep going!