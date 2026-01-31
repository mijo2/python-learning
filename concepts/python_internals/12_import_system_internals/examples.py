def run():
    print("=== Import System Internals Examples ===\n")

    # Example 1: sys.modules
    print("1. sys.modules cache:")
    import sys
    print(f"sys.modules keys (first 5): {list(sys.modules.keys())[:5]}")
    import os
    print(f"os in sys.modules: {'os' in sys.modules}")

    # Example 2: sys.path
    print("\n2. sys.path:")
    print(f"sys.path[0]: {sys.path[0]}")

    # Example 3: Dynamic import
    print("\n3. Dynamic import:")
    import importlib
    math_mod = importlib.import_module('math')
    print(f"math.pi: {math_mod.pi}")

    # Example 4: __import__
    print("\n4. Using __import__:")
    json_mod = __import__('json')
    print(f"json.dumps: {json_mod.dumps}")

    # Example 5: Reloading
    print("\n5. Reloading module:")
    # Create a simple module to reload
    # For demo, assume we have a module
    # import mymodule
    # importlib.reload(mymodule)

    print("Reload demo skipped (need external module)")

if __name__ == "__main__":
    run()