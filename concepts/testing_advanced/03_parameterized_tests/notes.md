# Parameterized Tests

## Overview
Parameterized tests allow running the same test logic with different input data, reducing code duplication and ensuring comprehensive test coverage across various scenarios.

## Pytest Parametrize
```python
import pytest

@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_square(input, expected):
    assert input ** 2 == expected
```

## Multiple Parameters
```python
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (4, 5, 9),
    (-1, 1, 0),
])
def test_addition(a, b, expected):
    assert add(a, b) == expected
```

## Parameter Names and IDs
```python
@pytest.mark.parametrize(
    "input,expected",
    [
        ("hello", "HELLO"),
        ("WORLD", "WORLD"),
        ("Python", "PYTHON"),
    ],
    ids=["lowercase", "uppercase", "mixed_case"]
)
def test_uppercase(input, expected):
    assert input.upper() == expected
```

## Combining Parametrize
```python
@pytest.mark.parametrize("base", [2, 10])
@pytest.mark.parametrize("exponent", [0, 1, 2, 3])
def test_power(base, exponent):
    result = base ** exponent
    assert isinstance(result, int)
```

## Fixtures with Parametrize
```python
@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.parametrize("x,y,expected", [
    (1, 2, 3),
    (4, 5, 9),
])
def test_calculator_add(calculator, x, y, expected):
    assert calculator.add(x, y) == expected
```

## Indirect Parametrization
```python
@pytest.fixture
def user_data(request):
    return {"name": request.param}

@pytest.mark.parametrize("user_data", ["Alice", "Bob", "Charlie"], indirect=True)
def test_user_creation(user_data):
    user = create_user(user_data)
    assert user.name in ["Alice", "Bob", "Charlie"]
```

## Dynamic Parametrization
```python
def generate_test_cases():
    cases = []
    for i in range(10):
        cases.append((i, i * 2))
    return cases

@pytest.mark.parametrize("input,expected", generate_test_cases())
def test_generated(input, expected):
    assert double(input) == expected
```

## Skipping and Conditional Tests
```python
@pytest.mark.parametrize("os_name,expected", [
    pytest.param("windows", "nt", marks=pytest.mark.skipif(
        not sys.platform.startswith("win"), reason="Windows only")),
    ("linux", "posix"),
    ("darwin", "posix"),
])
def test_os_detection(os_name, expected):
    assert os.name == expected
```

## Best Practices
- Use clear, descriptive parameter names
- Provide meaningful IDs for complex parameters
- Group related test cases together
- Use fixtures for complex setup
- Keep test functions simple and focused
