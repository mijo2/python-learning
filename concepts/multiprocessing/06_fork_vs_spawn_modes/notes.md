# Fork vs Spawn Modes

## Overview
Multiprocessing supports different start methods for creating child processes: fork, spawn, and forkserver. Each method has different performance characteristics, compatibility, and behavior.

## Fork Mode
- **Behavior**: Child process is exact copy of parent
- **Performance**: Fastest startup
- **Memory**: Copy-on-write, efficient memory usage
- **Platform**: Unix-like systems (Linux, macOS)
- **Default**: Python 3.3+ on Unix

```python
import multiprocessing as mp
mp.set_start_method('fork')

def worker():
    print("Child process")

p = mp.Process(target=worker)
p.start()
p.join()
```

## Spawn Mode
- **Behavior**: Fresh Python interpreter, imports executed
- **Performance**: Slower startup due to re-importing
- **Memory**: Clean process, no inherited state
- **Platform**: All platforms (Windows, Linux, macOS)
- **Default**: Windows, Python 3.4+ on macOS

## Forkserver Mode
- **Behavior**: Server process manages fork operations
- **Performance**: Moderate startup time
- **Security**: Better isolation
- **Platform**: Unix-like systems
- **Use Case**: High-security environments

## Choosing Start Method
```python
import multiprocessing as mp

# Check available methods
print(mp.get_all_start_methods())

# Set method (must be done before creating processes)
mp.set_start_method('spawn')  # or 'fork', 'forkserver'

# Context manager approach
ctx = mp.get_context('spawn')
queue = ctx.Queue()
process = ctx.Process(target=worker)
```

## Performance Comparison
```python
import time
import multiprocessing as mp

def benchmark_start_method(method):
    mp.set_start_method(method)
    start = time.time()
    processes = [mp.Process(target=lambda: None) for _ in range(10)]
    for p in processes: p.start()
    for p in processes: p.join()
    return time.time() - start

# Test different methods
for method in ['fork', 'spawn']:
    try:
        time_taken = benchmark_start_method(method)
        print(f"{method}: {time_taken:.3f}s")
    except RuntimeError:
        print(f"{method}: not available")
```

## Platform Differences
- **Windows**: Only 'spawn' available
- **Linux**: 'fork', 'spawn', 'forkserver'
- **macOS**: 'fork' (default), 'spawn'

## Considerations
- **Global State**: Fork copies, spawn doesn't
- **File Descriptors**: Fork inherits, spawn doesn't
- **Threading**: Fork copies threads, spawn doesn't
- **Security**: Spawn is safer

## Best Practices
- Use spawn for cross-platform compatibility
- Use fork for performance on Unix systems
- Set start method early in program
- Test on target platforms
- Consider security requirements
