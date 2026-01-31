"""
04 PROPERTY BASED TESTING — EXERCISES

Instructions:
- Learn about property-based testing with Hypothesis
- Implement functions that can be tested with property-based approaches
- Create tests that verify properties hold for many inputs
"""

# Exercise 1: Implement a function to test with properties
def reverse_string(text):
    """
    Reverse a string.

    Properties to test:
    - Reversing twice gives original: reverse(reverse(s)) == s
    - Length is preserved: len(reverse(s)) == len(s)
    - Characters are preserved: sorted(reverse(s)) == sorted(s)
    """
    return text[::-1]

# Exercise 2: Implement a sorting function with properties
def bubble_sort(arr):
    """
    Sort an array using bubble sort.

    Properties to test:
    - Result is sorted: all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
    - Same elements: sorted(arr) == sorted(original)
    - Length preserved: len(sorted_arr) == len(arr)
    """
    result = arr.copy()
    n = len(result)
    for i in range(n):
        for j in range(0, n-i-1):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
    return result

# Exercise 3: Implement a function that finds maximum
def find_maximum(numbers):
    """
    Find the maximum value in a list.

    Properties to test:
    - Result is in the list: max_val in numbers
    - All elements <= maximum: all(x <= max_val for x in numbers)
    - At least one element equals maximum: any(x == max_val for x in numbers)
    """
    if not numbers:
        raise ValueError("Empty list")
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val

# Exercise 4: Implement a simple calculator
def safe_divide(a, b):
    """
    Divide a by b, returning None if division by zero.

    Properties to test:
    - If b != 0, result * b ≈ a (within floating point precision)
    - If b == 0, result is None
    - Result is either None or a float
    """
    if b == 0:
        return None
    return a / b

# Exercise 5: Create a function to test string properties
def capitalize_words(text):
    """
    Capitalize the first letter of each word.

    Properties to test:
    - Result length equals input length
    - Only first letters are uppercase (if they were lowercase)
    - Non-first letters remain unchanged or become lowercase
    - Words are separated by spaces
    """
    return ' '.join(word.capitalize() for word in text.split())

if __name__ == "__main__":
    # Test the functions manually
    print("Testing reverse_string:")
    test_str = "Hello World"
    reversed_str = reverse_string(test_str)
    print(f"Original: {test_str}")
    print(f"Reversed: {reversed_str}")
    print(f"Double reverse: {reverse_string(reversed_str)}")
    print()

    print("Testing bubble_sort:")
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort(test_arr)
    print(f"Original: {test_arr}")
    print(f"Sorted: {sorted_arr}")
    print(f"Is sorted: {all(sorted_arr[i] <= sorted_arr[i+1] for i in range(len(sorted_arr)-1))}")
    print()

    print("Testing find_maximum:")
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    max_val = find_maximum(numbers)
    print(f"Numbers: {numbers}")
    print(f"Maximum: {max_val}")
    print()

    print("Testing safe_divide:")
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")
    print()

    print("Testing capitalize_words:")
    text = "hello world python programming"
    capitalized = capitalize_words(text)
    print(f"Original: {text}")
    print(f"Capitalized: {capitalized}")
