
def run():
    print("=== 08 CONTRACT TESTING Examples ===
")

    # Example 1: Basic test structure
    print("1. Basic Test Structure:")
    print("   def test_example():")
    print("       assert True")

    print()

    # Example 2: Using fixtures
    print("2. Using Fixtures:")
    print("   @pytest.fixture")
    print("   def sample_data():")
    print("       return {'key': 'value'}")
    print()
    print("   def test_with_fixture(sample_data):")
    print("       assert sample_data['key'] == 'value'")

    print()

    # Example 3: Parameterized tests
    print("3. Parameterized Tests:")
    print("   @pytest.mark.parametrize('input,expected', [")
    print("       (1, 2),")
    print("       (2, 4),")
    print("   ])")
    print("   def test_double(input, expected):")
    print("       assert input * 2 == expected")

if __name__ == "__main__":
    run()
