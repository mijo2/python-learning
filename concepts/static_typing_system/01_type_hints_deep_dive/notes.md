# Type Hints Deep Dive

**Type hints** add static typing to Python, improving code clarity and catching errors early with tools like mypy.

## Basic Type Hints

```python
def greet(name: str) -> str:
    return f"Hello {name}"

age: int = 25
```

- **Function Annotations**: `param: Type -> ReturnType`
- **Variable Annotations**: `var: Type`

## Advanced Hints

1. **Union**: Multiple types.
   ```python
   from typing import Union
   def process(data: Union[str, int]) -> str:
       return str(data)
   ```

2. **Optional**: None allowed.
   ```python
   from typing import Optional
   def find(name: str) -> Optional[int]:
       return None
   ```

3. **List/Dict**: Generic types.
   ```python
   from typing import List, Dict
   names: List[str] = ["Alice"]
   mapping: Dict[str, int] = {"a": 1}
   ```

4. **Any**: No type checking.
   ```python
   from typing import Any
   data: Any = "anything"
   ```

## Benefits

- **IDE Support**: Autocomplete, refactoring.
- **Documentation**: Self-documenting code.
- **Error Detection**: Catch bugs at development time.

Use mypy to check: `mypy script.py`. Experiment with hints in functions. This builds type safety—next, generics.