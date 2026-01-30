# Multiple Inheritance and MRO Exercises Solutions

class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    pass

# Test
c = C()
c.greet()  # Hello from A