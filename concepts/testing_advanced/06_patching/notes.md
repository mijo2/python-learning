# Patching in Testing

## Overview
Patching temporarily replaces attributes, functions, or objects during testing. It's a powerful technique for isolating code under test and controlling external dependencies.

## patch Decorator
```python
from unittest.mock import patch

@patch('module.function_to_patch')
def test_with_patch(mock_function):
    mock_function.return_value = "patched"

    result = code_under_test()
    assert result == "expected"
    mock_function.assert_called_once()
```

## patch Context Manager
```python
def test_context_patch():
    with patch('module.external_call') as mock_call:
        mock_call.return_value = {"data": "mocked"}

        result = function_that_calls_external()
        assert result["data"] == "mocked"
```

## Patching Import Paths
```python
# Patch module import
@patch('mypackage.mymodule.SomeClass')
def test_class_patching(mock_class):
    mock_instance = mock_class.return_value
    mock_instance.method.return_value = "mocked"

    result = use_some_class()
    assert result == "mocked"
```

## Multiple Patches
```python
@patch('module.func1')
@patch('module.func2')
def test_multiple_patches(mock_func2, mock_func1):
    # Note: decorators are applied bottom-up
    mock_func1.return_value = "func1"
    mock_func2.return_value = "func2"

    result = code_using_both()
    assert result == "expected"
```

## patch.object
```python
from unittest.mock import patch

class MyClass:
    def method(self):
        return "real"

def test_patch_method():
    obj = MyClass()

    with patch.object(obj, 'method', return_value="mocked"):
        assert obj.method() == "mocked"

    # Original method restored
    assert obj.method() == "real"
```

## patch.dict
```python
def test_patch_dict():
    my_dict = {"key": "original"}

    with patch.dict(my_dict, {"key": "patched", "new_key": "new"}):
        assert my_dict["key"] == "patched"
        assert my_dict["new_key"] == "new"

    # Dict restored
    assert my_dict == {"key": "original"}
```

## Patching Built-ins
```python
def test_patch_builtin():
    with patch('builtins.open') as mock_open:
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = "mocked content"

        with open('file.txt') as f:
            content = f.read()

        assert content == "mocked content"
        mock_open.assert_called_with('file.txt')
```

## Autospec
```python
# Preserve original function signature
@patch('module.function', autospec=True)
def test_with_autospec(mock_func):
    # mock_func now has same signature as original
    try:
        mock_func(wrong_arg="value")  # TypeError
    except TypeError:
        pass  # Expected
```

## Best Practices
- Patch at the point of use, not definition
- Use autospec to catch signature mismatches
- Keep patches focused and minimal
- Document what is being patched and why
- Avoid over-patching - test real code when possible
