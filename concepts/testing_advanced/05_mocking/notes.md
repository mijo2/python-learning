# Mocking in Testing

## Overview
Mocking replaces real objects with fake ones during testing, allowing isolation of code under test and control over dependencies. This enables testing components in isolation and simulating various scenarios.

## unittest.mock Basics
```python
from unittest.mock import Mock, MagicMock
import pytest

def test_function_with_mock():
    # Create a mock object
    mock_obj = Mock()
    mock_obj.method.return_value = "mocked result"

    # Use in test
    result = function_under_test(mock_obj)
    assert result == "expected result"
    mock_obj.method.assert_called_once()
```

## Mock Types
- **Mock**: Basic mock object
- **MagicMock**: Mock with magic method support
- **patch**: Context manager/decorator for patching
- **PropertyMock**: Mock object properties
- **AsyncMock**: For async functions

## Patching Functions
```python
from unittest.mock import patch

def test_external_api_call():
    with patch('module.external_api') as mock_api:
        mock_api.return_value = {"status": "success"}

        result = call_external_api()
        assert result["status"] == "success"
        mock_api.assert_called_with(expected_params)
```

## Mock Side Effects
```python
def test_mock_side_effects():
    mock = Mock()
    # Return different values on successive calls
    mock.side_effect = [1, 2, 3, Exception("error")]

    assert mock() == 1
    assert mock() == 2
    assert mock() == 3
    with pytest.raises(Exception):
        mock()
```

## Async Mocking
```python
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_async_function():
    mock = AsyncMock()
    mock.return_value = "async result"

    result = await async_function_under_test(mock)
    assert result == "async result"
    mock.assert_awaited_once()
```

## Property Mocking
```python
from unittest.mock import PropertyMock, patch

def test_property_mocking():
    with patch('module.MyClass.property', new_callable=PropertyMock) as mock_prop:
        mock_prop.return_value = "mocked value"

        obj = MyClass()
        assert obj.property == "mocked value"
```

## Mock Configuration
```python
def test_detailed_mock():
    mock = Mock()
    mock.configure_mock(**{
        'method.return_value': 'value',
        'attribute': 'attr_value',
        'method.side_effect': lambda x: x * 2
    })

    assert mock.method(5) == 10
    assert mock.attribute == 'attr_value'
```

## Best Practices
- Mock at the boundary (external dependencies)
- Don't mock everything - test real code when possible
- Use descriptive mock names
- Verify mock interactions
- Keep mocks simple and focused
