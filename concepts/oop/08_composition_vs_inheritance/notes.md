# Composition vs Inheritance (Pythonic Design)

Superb! Mixins showed you composable inheritance. Now, let's compare **composition** and **inheritance**—two ways to build complex objects. Inheritance is "is-a" (Car is-a Vehicle), while composition is "has-a" (Car has-an Engine). Python favors composition for its flexibility and maintainability.

Choose wisely: inheritance for hierarchies, composition for flexibility.

## Inheritance Recap

Tight coupling: Subclass inherits all behavior.

```python
class Engine:
    def start(self):
        print("Engine started")

class Car(Engine):  # Car IS-A Engine
    pass

car = Car()
car.start()  # Inherits start()
```

Pros: Simple, automatic inheritance.
Cons: Rigid—changes to Engine affect Car. Deep hierarchies become fragile.

## Composition

Loose coupling: Class contains other objects.

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine

    def start(self):
        self.engine.start()

car = Car()
car.start()  # Delegates to engine
```

Pros: Flexible—swap engines easily. Easier testing/mocking.
Cons: More code (delegation).

## When to Use Which?

- **Inheritance**: "Is-a" relationships (e.g., Dog is-a Animal). Use for polymorphism.
- **Composition**: "Has-a" relationships (e.g., Car has-a GPS). Use for modularity.

Pythonic: "Favor composition over inheritance" (Gang of Four).

## Advanced Composition

1. **Delegation**: Forward calls to contained objects.
2. **Strategy Pattern**: Swap behaviors at runtime.
3. **Mixin Alternative**: Composition with mixins for features.

Example: Configurable Car.

```python
class ElectricEngine:
    def start(self):
        print("Electric engine started")

class Car:
    def __init__(self, engine_type):
        if engine_type == "electric":
            self.engine = ElectricEngine()
        else:
            self.engine = Engine()

    def start(self):
        self.engine.start()

car = Car("electric")
car.start()  # Electric engine started
```

## Best Practices

- **Composition First**: Default to "has-a".
- **Shallow Inheritance**: Limit to 2-3 levels.
- **Interfaces**: Use protocols/ABCs for contracts.
- **Testability**: Composition eases mocking.

## Pitfalls

1. **Over-Inheritance**: Leads to fragile base class problem.
2. **Composition Boilerplate**: Can be verbose—use properties.

Refactor a previous inheritance example to use composition. Compare the pros/cons. This ties into dataclasses next. You're designing like a pro—excellent work!