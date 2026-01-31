# Property-Based Testing

## Overview
Property-based testing generates random test inputs to verify that certain properties hold true for a wide range of data. Instead of testing specific examples, it tests general behaviors and invariants.

## Basic Hypothesis Usage
```python
from hypothesis import given
import hypothesis.strategies as st

@given(st.integers())
def test_absolute_value(x):
    result = abs(x)
    assert result >= 0
    if x == 0:
        assert result == 0
    else:
        assert result > 0
```

## Strategies for Data Generation
```python
from hypothesis import given, strategies as st

@given(
    st.lists(st.integers(), min_size=1),
    st.functions()
)
def test_list_operations(data, func):
    # Test properties of list operations
    original = data.copy()
    result = [func(x) for x in data]
    assert len(result) == len(data)
```

## Common Strategies
- **Primitives**: `st.integers()`, `st.floats()`, `st.booleans()`
- **Collections**: `st.lists()`, `st.dictionaries()`, `st.sets()`
- **Text**: `st.text()`, `st.characters()`
- **Complex**: `st.datetimes()`, `st.emails()`
- **Custom**: `st.from_type()`, `st.register_type_strategy()`

## Property Examples
```python
@given(st.lists(st.integers()))
def test_sort_properties(data):
    sorted_data = sorted(data)
    # Properties that should always hold
    assert len(sorted_data) == len(data)
    assert all(sorted_data[i] <= sorted_data[i+1] for i in range(len(sorted_data)-1))

@given(st.text(), st.text())
def test_string_concatenation(s1, s2):
    result = s1 + s2
    assert len(result) == len(s1) + len(s2)
    assert result.startswith(s1)
    assert result.endswith(s2)
```

## Shrinking and Debugging
```python
# Hypothesis will try to find the smallest failing example
@given(st.lists(st.integers(min_value=0)))
def test_sum_positive(numbers):
    # This might fail for large lists
    total = sum(numbers)
    assert total >= 0  # Fails if list contains very large negative numbers
```

## State Machine Testing
```python
from hypothesis.stateful import RuleBasedStateMachine, rule, precondition

class StackMachine(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.stack = []

    @rule(value=st.integers())
    def push(self, value):
        self.stack.append(value)

    @rule()
    @precondition(lambda self: len(self.stack) > 0)
    def pop(self):
        self.stack.pop()

    @rule()
    def check_invariants(self):
        assert len(self.stack) >= 0
        # Other invariant checks
```

## Integration with Pytest
```python
# settings for hypothesis
from hypothesis import settings, Phase

@given(st.integers())
@settings(
    max_examples=1000,
    phases=[Phase.generate, Phase.shrink, Phase.explain]
)
def test_my_function(x):
    assert my_function(x) > 0
```

## Advantages
- **Comprehensive Coverage**: Tests many more cases than manual tests
- **Bug Discovery**: Finds edge cases and unexpected inputs
- **Specification Clarity**: Forces thinking about invariants
- **Regression Prevention**: Catches bugs from code changes

## Best Practices
- Focus on properties, not specific examples
- Use appropriate strategies for your domain
- Handle edge cases explicitly when needed
- Combine with traditional unit tests
- Review and minimize failing examples
