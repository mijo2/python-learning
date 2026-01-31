def run():
    print("=== Attribute Lookup Chain Examples ===\n")

    # Example 1: Instance vs class attributes
    print("1. Instance overrides class:")
    class A:
        x = "class"

    obj = A()
    print(f"obj.x (class): {obj.x}")
    obj.x = "instance"
    print(f"obj.x (instance): {obj.x}")
    print(f"A.x (class): {A.x}")

    # Example 2: MRO in inheritance
    print("\n2. MRO in inheritance:")
    class B(A):
        x = "B class"

    obj2 = B()
    print(f"obj2.x: {obj2.x}")  # B's x
    print(f"B.__mro__: {B.__mro__}")

    # Example 3: Descriptors override instance
    print("\n3. Descriptors override:")
    class Descriptor:
        def __get__(self, instance, owner):
            return "from descriptor"

        def __set__(self, instance, value):
            pass  # Data descriptor

    class C:
        attr = Descriptor()

    c = C()
    c.attr = "instance value"
    print(f"c.attr: {c.attr}")  # descriptor, not instance

    # Example 4: Non-data descriptor
    print("\n4. Non-data descriptor:")
    class NonDataDesc:
        def __get__(self, instance, owner):
            return "non-data desc"

    class D:
        attr = NonDataDesc()

    d = D()
    d.attr = "instance"
    print(f"d.attr: {d.attr}")  # instance wins over non-data desc

    # Example 5: __getattr__
    print("\n5. __getattr__:")
    class E:
        def __getattr__(self, name):
            return f"dynamic_{name}"

    e = E()
    print(f"e.anything: {e.anything}")

if __name__ == "__main__":
    run()