# Pathlib Patterns

## Overview
The `pathlib` module provides object-oriented filesystem paths. It offers a more intuitive and cross-platform way to work with file paths compared to string manipulation.

## Basic Path Operations
```python
from pathlib import Path

# Create paths
path = Path("folder/file.txt")
absolute_path = Path("/home/user/file.txt")

# Current directory
current = Path.cwd()

# Home directory
home = Path.home()
```

## Path Navigation
```python
# Joining paths
config_path = Path("~/.config").expanduser() / "app" / "settings.json"

# Parent directories
parent = config_path.parent
grandparent = config_path.parents[1]

# Path components
print(config_path.parts)  # ('/', 'home', 'user', '.config', 'app', 'settings.json')
print(config_path.name)   # 'settings.json'
print(config_path.stem)   # 'settings'
print(config_path.suffix) # '.json'
```

## File Operations
```python
file_path = Path("data.txt")

# Check existence and type
print(file_path.exists())
print(file_path.is_file())
print(file_path.is_dir())

# Read/write operations
file_path.write_text("Hello, World!")
content = file_path.read_text()

# Binary operations
file_path.write_bytes(b"binary data")
data = file_path.read_bytes()
```

## Directory Operations
```python
dir_path = Path("project")

# Create directories
dir_path.mkdir(parents=True, exist_ok=True)

# List contents
for item in dir_path.iterdir():
    if item.is_file():
        print(f"File: {item}")
    elif item.is_dir():
        print(f"Directory: {item}")

# Recursive listing
for file_path in dir_path.rglob("*.py"):
    print(f"Python file: {file_path}")
```

## Pattern Matching
```python
# Glob patterns
for txt_file in Path(".").glob("*.txt"):
    print(txt_file)

# Recursive glob
for py_file in Path("src").rglob("*.py"):
    print(py_file)

# Complex patterns
for file in Path(".").glob("**/*.log"):
    print(file)
```

## Path Manipulation
```python
path = Path("folder/subfolder/file.txt")

# Relative paths
relative = path.relative_to("folder")

# Resolve to absolute path
absolute = path.resolve()

# Change suffix
new_path = path.with_suffix(".bak")

# Change name
renamed = path.with_name("new_file.txt")
```

## Cross-Platform Compatibility
```python
# Pathlib handles OS differences automatically
path = Path("folder") / "file.txt"  # Uses correct separator

# Works on Windows, Linux, macOS
config_dir = Path.home() / ".config" / "myapp"
```

## Best Practices
- Use Path objects instead of string paths
- Leverage path operations over string manipulation
- Use `resolve()` for absolute paths
- Handle exceptions for file operations
- Use context managers for temporary files
