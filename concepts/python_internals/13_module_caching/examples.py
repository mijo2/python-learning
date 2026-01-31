def run():
    print("=== Module Caching Examples ===\n")

    # Example 1: sys.modules cache
    import sys
    print("1. Modules in cache:")
    print(f"Number of cached modules: {len(sys.modules)}")
    print(f"'os' cached: {'os' in sys.modules}")

    # Example 2: Importing adds to cache
    print("\n2. Importing adds to cache:")
    before = len(sys.modules)
    import math
    after = len(sys.modules)
    print(f"Modules before: {before}, after: {after}")
    print(f"math in cache: {'math' in sys.modules}")

    # Example 3: Re-import uses cache
    print("\n3. Re-import uses cache:")
    import math  # Already imported
    print("Re-imported math, still same object")

    # Example 4: Check identity
    print("\n4. Module identity:")
    import json
    import json as j
    print(f"json is j: {json is j}")  # True, same object

    # Example 5: Remove from cache
    print("\n5. Removing from cache:")
    print(f"Before: 'json' in sys.modules: {'json' in sys.modules}")
    del sys.modules['json']
    print(f"After: 'json' in sys.modules: {'json' in sys.modules}")

if __name__ == "__main__":
    run()