def run():
    print("=== Mutability Rules Examples ===\n")

    # Example 1: Immutable integers
    print("1. Immutable integers:")
    x = 10
    y = x
    x = x + 1
    print(f"x: {x}, y: {y}")  # x: 11, y: 10

    # Example 2: Mutable lists
    print("\n2. Mutable lists:")
    lst1 = [1, 2, 3]
    lst2 = lst1  # Both point to same list
    lst1.append(4)
    print(f"lst1: {lst1}, lst2: {lst2}")  # Both modified

    # Example 3: Strings are immutable
    print("\n3. Strings are immutable:")
    s1 = "hello"
    s2 = s1
    s1 = s1.upper()
    print(f"s1: {s1}, s2: {s2}")  # s1: HELLO, s2: hello

    # Example 4: Tuples are immutable
    print("\n4. Tuples are immutable:")
    t1 = (1, 2, [3, 4])
    # t1[0] = 5  # TypeError: 'tuple' object does not support item assignment
    print(f"t1: {t1}")
    # But inner list is mutable
    t1[2].append(5)
    print(f"t1 after modifying inner list: {t1}")

    # Example 5: Default mutable arguments pitfall
    print("\n5. Default mutable arguments:")
    def append_to_list(item, lst=[]):
        lst.append(item)
        return lst

    print(append_to_list(1))  # [1]
    print(append_to_list(2))  # [1, 2] - same list!
    print(append_to_list(3, []))  # [3] - new list

if __name__ == "__main__":
    run()