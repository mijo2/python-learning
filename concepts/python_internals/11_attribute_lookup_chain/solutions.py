"""
ATTRIBUTE LOOKUP CHAIN — SOLUTIONS
"""

# Exercise 1: Instance vs class
class Test1:
    value = "class"

obj1 = Test1()
print("Ex1: obj1.value =", obj1.value)  # class
obj1.value = "instance"
print("Ex1: obj1.value =", obj1.value)  # instance
print("Ex1: Test1.value =", Test1.value)  # class

# Exercise 2: Inheritance
class Parent:
    attr = "parent"

class Child(Parent):
    pass

c = Child()
print("Ex2: c.attr =", c.attr)  # parent

# Exercise 3: Descriptor precedence
class DataDesc:
    def __get__(self, instance, owner):
        return "desc"
    def __set__(self, instance, value):
        pass  # Makes it data descriptor

class Test3:
    x = DataDesc()

t = Test3()
t.x = "instance"
print("Ex3: t.x =", t.x)  # desc (data desc wins)

# Exercise 4: Non-data desc
class NonData:
    def __get__(self, instance, owner):
        return "non-data"

class Test4:
    y = NonData()

t4 = Test4()
print("Ex4: t4.y =", t4.y)  # non-data
t4.y = "inst"
print("Ex4: t4.y =", t4.y)  # inst (instance wins over non-data)

# Exercise 5: __getattribute__
class Test5:
    def __init__(self):
        self.normal = "normal"

    def __getattribute__(self, name):
        if name == "special":
            return "special value"
        return super().__getattribute__(name)

t5 = Test5()
print("Ex5: t5.normal =", t5.normal)
print("Ex5: t5.special =", t5.special)