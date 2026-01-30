# Pytest Advanced Features

**Pytest** is Python's premier testing framework. It simplifies writing and running tests with powerful features.

## Basic Pytest

```python
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
```

Run with `pytest`.

## Advanced Features

1. **Fixtures**: Setup/teardown reusable code.
   ```python
   import pytest

   @pytest.fixture
   def sample_data():
       return [1, 2, 3]

   def test_sum(sample_data):
       assert sum(sample_data) == 6
   ```

2. **Parameterized Tests**: Run test with multiple inputs.
   ```python
   @pytest.mark.parametrize("a,b,expected", [(1,2,3), (0,0,0)])
   def test_add(a, b, expected):
       assert add(a, b) == expected
   ```

3. **Marks**: Categorize tests.
   ```python
   @pytest.mark.slow
   def test_slow():
       pass
   # Run: pytest -m "not slow"
   ```

## Why Pytest?

- **Simple**: No boilerplate.
- **Powerful**: Fixtures, plugins, parallel execution.
- **Extensible**: Custom plugins.

Experiment with fixtures and parametrization. This builds robust tests—next, fixtures deep dive.