# Multiple Inheritance and MRO Examples

class A:
    def method(self):
        print("A")

class B:
    def method(self):
        print("B")

class C(A, B):
    pass

c = C()
c.method()  # A (due to MRO: C -> A -> B -> object)
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)