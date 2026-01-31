# Object Model Examples

class MyClass:
    class_attr = "shared"

obj1 = MyClass()
obj2 = MyClass()

obj1.instance_attr = "unique"

print("Class dict:", MyClass.__dict__)
print("Obj1 dict:", obj1.__dict__)
print("Obj2 dict:", obj2.__dict__)

print("Type of class:", type(MyClass))
print("Type of obj:", type(obj1))