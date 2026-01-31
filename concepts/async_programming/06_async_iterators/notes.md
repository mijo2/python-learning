# Async Iterators

## Overview
Async iterators allow iteration over asynchronous data sources, where each iteration step may involve async operations. They provide `async for` syntax for clean, readable asynchronous iteration.

## Basic Async Iterator
```python
class AsyncCounter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current >= self.limit:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)  # Simulate async operation
        self.current += 1
        return self.current

async def use_async_iterator():
    async for number in AsyncCounter(5):
        print(f"Got: {number}")

asyncio.run(use_async_iterator())
```

## Async Iterator Protocol
- **`__aiter__(self)`**: Returns async iterator object
- **`__anext__(self)`**: Returns awaitable yielding next value or raises `StopAsyncIteration`

## Async Generator (Preferred)
```python
async def async_range(n):
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

async def use_async_generator():
    async for value in async_range(5):
        print(f"Value: {value}")
```

## Real-world Examples
```python
# Database result streaming
async def fetch_rows(query):
    connection = await create_db_connection()
    cursor = await connection.cursor()
    await cursor.execute(query)

    async for row in cursor:
        yield row

    await cursor.close()
    await connection.close()

# File reading line by line
async def read_lines_async(filename):
    async with aiofiles.open(filename, 'r') as file:
        async for line in file:
            yield line.strip()

# API pagination
async def paginated_api_results(api_url):
    page = 1
    while True:
        response = await fetch_page(api_url, page)
        for item in response['items']:
            yield item

        if not response['has_next']:
            break
        page += 1
```

## Async Comprehensions
```python
async def async_comprehension_example():
    # Async list comprehension
    squares = [x async for x in async_range(5) if x % 2 == 0]
    print(squares)  # [0, 4, 8, 12, 16]

    # Async dict comprehension
    async def async_pairs():
        async for i in async_range(3):
            yield i, i**2

    pairs = {k: v async for k, v in async_pairs()}
    print(pairs)  # {0: 0, 1: 1, 2: 4}
```

## Async Iterable vs Async Iterator
- **Async Iterable**: Has `__aiter__` method
- **Async Iterator**: Has `__aiter__` and `__anext__` methods

## Converting Sync to Async
```python
class AsyncIteratorWrapper:
    def __init__(self, iterable):
        self.iterable = iter(iterable)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            return next(self.iterable)
        except StopIteration:
            raise StopAsyncIteration
```

## Exception Handling
```python
async def handle_iterator_exceptions():
    async for item in potentially_failing_iterator():
        try:
            await process_item(item)
        except ValueError:
            continue  # Skip bad items
        except Exception as e:
            print(f"Processing failed: {e}")
            break
```

## Performance Considerations
- **Eager vs Lazy**: Async iterators are lazy by default
- **Buffering**: Consider buffering for performance
- **Cancellation**: Handle cancellation properly
- **Resource Management**: Clean up resources

## Best Practices
- Use async generators when possible
- Handle `StopAsyncIteration` properly
- Implement proper cleanup in async iterators
- Test with cancellation scenarios
- Prefer async iterators over manual async loops
