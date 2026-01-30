# Dataclasses & attrs Exercises

# Exercise: Dataclasses
# Use dataclass to create a 'Student' with name, age, grades (list).

# TODO: Implement Student dataclass
from dataclasses import dataclass, field

@dataclass
class Student:
    pass

# Test
# student = Student("Alice", 20)
# student.grades.append(85)
# print(student)