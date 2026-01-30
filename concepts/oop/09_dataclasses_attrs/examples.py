# Dataclasses & attrs Examples

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

person = Person("Alice", 30)
print(person)  # Person(name='Alice', age=30)

from dataclasses import dataclass, field

@dataclass
class Employee:
    name: str
    age: int
    salary: float = field(default=50000, repr=False)
    skills: list = field(default_factory=list)

emp = Employee("Bob", 25)
emp.skills.append("Python")
print(emp)

# attrs Library (requires installation)
try:
    import attr

    @attr.s
    class Person:
        name = attr.ib()
        age = attr.ib()

    @attr.s
    class Employee(Person):
        salary = attr.ib()

    emp = Employee("Charlie", 35, 60000)
    print(emp)
except ImportError:
    print("attrs not installed")