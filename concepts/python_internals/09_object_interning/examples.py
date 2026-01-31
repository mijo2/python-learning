def run():
    print("=== Object Interning Examples ===\n")

    # Example 1: Small integers
    print("1. Small integers (-5 to 256):")
    a = 100
    b = 100
    print(f"a is b: {a is b}")  # True

    c = 300
    d = 300
    print(f"c is d: {c is d}")  # False

    # Example 2: Strings
    print("\n2. String interning:")
    s1 = "python"
    s2 = "python"
    print(f"s1 is s2: {s1 is s2}")  # True

    s3 = "python rocks"
    s4 = "python rocks"
    print(f"s3 is s4: {s3 is s4}")  # False (contains space)

    # Example 3: Using sys.intern
    print("\n3. Manual interning with sys.intern:")
    import sys
    interned_str = sys.intern("manual interning")
    another = "manual interning"
    print(f"interned_str is another: {interned_str is another}")  # False, but if assigned same, yes

    # Better example
    key1 = sys.intern("key")
    key2 = sys.intern("key")
    print(f"key1 is key2: {key1 is key2}")  # True

    # Example 4: Identity vs equality
    print("\n4. Identity vs equality:")
    x = [1, 2, 3]
    y = [1, 2, 3]
    print(f"x == y: {x == y}")  # True
    print(f"x is y: {x is y}")  # False

    z = x
    print(f"x is z: {x is z}")  # True

if __name__ == "__main__":
    run()