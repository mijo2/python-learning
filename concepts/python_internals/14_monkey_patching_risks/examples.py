def run():
    print("=== Monkey Patching Risks Examples ===\n")

    # Example 1: Simple function patching
    print("1. Patching a function:")
    def original_func():
        return "original"

    print(f"Before: {original_func()}")

    # Monkey patch
    original_func = lambda: "patched"
    print(f"After: {original_func()}")

    # Example 2: Patching module function
    print("\n2. Patching module function:")
    import math
    original_sin = math.sin
    math.sin = lambda x: 0  # Bad patch
    print(f"math.sin(0): {math.sin(0)}")
    # Restore
    math.sin = original_sin

    # Example 3: Adding method to class
    print("\n3. Adding method to class:")
    class MyClass:
        pass

    obj = MyClass()
    # obj.new_method()  # AttributeError

    def new_method(self):
        return "added dynamically"

    MyClass.new_method = new_method
    print(f"obj.new_method(): {obj.new_method()}")

    # Example 4: Patching built-in
    print("\n4. Patching built-in (dangerous):")
    original_len = len
    len = lambda x: 0  # Very bad
    print(f"len([1,2,3]): {len([1,2,3])}")
    # Restore
    len = original_len

    print("\nNote: Monkey patching can break other code!")

if __name__ == "__main__":
    run()