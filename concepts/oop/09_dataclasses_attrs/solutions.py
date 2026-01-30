# Dataclasses & attrs Exercises Solutions

from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    age: int
    grades: list = field(default_factory=list)

# Test
student = Student("Alice", 20)
student.grades.append(85)
print(student)  # Student(name='Alice', age=20, grades=[85])