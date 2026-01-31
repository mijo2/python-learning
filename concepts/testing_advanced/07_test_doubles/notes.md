# Test Doubles

## Overview
Test doubles are objects that replace real dependencies during testing. They help isolate code under test and control test scenarios. There are several types of test doubles with different purposes.

## Types of Test Doubles

### Dummy
- **Purpose**: Satisfy method signatures, not used in test
- **Example**: Fill parameter lists
```python
def test_function(dummmy_param=None):
    # dummy_param is never used
    assert True
```

### Stub
- **Purpose**: Provide canned responses to method calls
- **Example**: Return fixed data
```python
class DatabaseStub:
    def get_user(self, user_id):
        return {"id": user_id, "name": "Stub User"}
```

### Spy
- **Purpose**: Record method calls for later verification
- **Example**: Track interactions
```python
class EmailServiceSpy:
    def __init__(self):
        self.sent_emails = []

    def send_email(self, to, subject, body):
        self.sent_emails.append({"to": to, "subject": subject, "body": body})
        return True
```

### Mock
- **Purpose**: Verify expectations and provide canned responses
- **Example**: Full behavior control
```python
from unittest.mock import Mock

mock_service = Mock()
mock_service.process.return_value = "success"
mock_service.process.side_effect = ValueError("error")

# Use in test
result = function_under_test(mock_service)
mock_service.process.assert_called_with(expected_args)
```

### Fake
- **Purpose**: Working implementation with shortcuts
- **Example**: In-memory database
```python
class FakeDatabase:
    def __init__(self):
        self.data = {}

    def save(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)
```

## Choosing the Right Double
- **Dummy**: When you need to satisfy interfaces but don't care about behavior
- **Stub**: When you need predictable responses
- **Spy**: When you need to verify interactions
- **Mock**: When you need full control and verification
- **Fake**: When you need realistic but simplified behavior

## Implementation with unittest.mock
```python
from unittest.mock import Mock, MagicMock

# Basic mock
mock_obj = Mock()
mock_obj.method.return_value = "response"

# Magic mock (supports magic methods)
magic_mock = MagicMock()
magic_mock.__str__.return_value = "string representation"

# Spec to match real object
real_obj = RealClass()
mock_with_spec = Mock(spec=real_obj)
```

## Best Practices
- Use the simplest double that meets your needs
- Prefer real objects over doubles when possible
- Make doubles obvious in tests (naming conventions)
- Don't test the double itself
- Keep doubles focused on their purpose
