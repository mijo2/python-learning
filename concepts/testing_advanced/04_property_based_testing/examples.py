
def run():
    print("=== 04 PROPERTY BASED TESTING Examples ===\n")

    # Example 1: Functions designed for property-based testing
    print("1. Functions with Testable Properties:")

    def reverse_string(text):
        """Reverse a string."""
        return text[::-1]

    def bubble_sort(arr):
        """Sort an array using bubble sort."""
        result = arr.copy()
        n = len(result)
        for i in range(n):
            for j in range(0, n-i-1):
                if result[j] > result[j+1]:
                    result[j], result[j+1] = result[j+1], result[j]
        return result

    def find_maximum(numbers):
        """Find the maximum value in a list."""
        if not numbers:
            raise ValueError("Empty list")
        max_val = numbers[0]
        for num in numbers[1:]:
            if num > max_val:
                max_val = num
        return max_val

    def safe_divide(a, b):
        """Divide a by b, returning None if division by zero."""
        if b == 0:
            return None
        return a / b

    def capitalize_words(text):
        """Capitalize the first letter of each word."""
        return ' '.join(word.capitalize() for word in text.split())

    # Demonstrate the functions
    print("   reverse_string('hello') =", reverse_string("hello"))
    print("   bubble_sort([3,1,4,1,5]) =", bubble_sort([3,1,4,1,5]))
    print("   find_maximum([1,3,2,5,4]) =", find_maximum([1,3,2,5,4]))
    print("   safe_divide(10, 2) =", safe_divide(10, 2))
    print("   safe_divide(10, 0) =", safe_divide(10, 0))
    print("   capitalize_words('hello world') =", capitalize_words("hello world"))

    print()

    # Example 2: Property-based testing with Hypothesis
    print("2. Property-Based Testing with Hypothesis:")

    try:
        from hypothesis import given, strategies as st

        @given(st.text())
        def test_reverse_properties(text):
            """Test properties of string reversal"""
            reversed_text = reverse_string(text)
            double_reversed = reverse_string(reversed_text)

            assert len(reversed_text) == len(text)
            assert double_reversed == text
            assert sorted(reversed_text) == sorted(text)

        @given(st.lists(st.integers()))
        def test_sort_properties(arr):
            """Test properties of sorting"""
            sorted_arr = bubble_sort(arr)

            # Length preserved
            assert len(sorted_arr) == len(arr)

            # Same elements
            assert sorted(sorted_arr) == sorted(arr)

            # Is sorted
            for i in range(len(sorted_arr) - 1):
                assert sorted_arr[i] <= sorted_arr[i + 1]

        print("   Running property tests...")

        # Run a few examples
        test_reverse_properties()
        test_sort_properties()

        print("   ✓ Property tests passed")

    except ImportError:
        print("   Hypothesis not available - install with: pip install hypothesis")

    print()

    # Example 3: Manual property verification
    print("3. Manual Property Verification:")

    test_cases = [
        ("hello", "olleh"),
        ("", ""),
        ("a", "a"),
        ("123", "321")
    ]

    print("   String reversal properties:")
    for original, expected in test_cases:
        reversed_str = reverse_string(original)
        double_reversed = reverse_string(reversed_str)

        # Check properties
        length_ok = len(reversed_str) == len(original)
        double_reverse_ok = double_reversed == original
        chars_ok = sorted(reversed_str) == sorted(original)

        status = "✓" if all([length_ok, double_reverse_ok, chars_ok]) else "✗"
        print(f"   '{original}' -> '{reversed_str}' {status}")

if __name__ == "__main__":
    run()
