# Non-Blocking IO in Async Programming

## Overview
Non-blocking IO allows programs to perform IO operations without waiting for them to complete, enabling high concurrency. Async programming builds on non-blocking IO to handle thousands of concurrent connections efficiently.

## Synchronous vs Asynchronous IO
```python
import requests
import asyncio
import aiohttp

# Synchronous (blocking)
def sync_download(urls):
    results = []
    for url in urls:
        response = requests.get(url)  # Blocks until complete
        results.append(response.text)
    return results

# Asynchronous (non-blocking)
async def async_download(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch(session, url))
        results = await asyncio.gather(*tasks)
        return results

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()
```

## How Non-Blocking IO Works
- **Event Loop**: Monitors multiple IO operations
- **Readiness Notification**: OS notifies when IO is ready
- **Cooperative Multitasking**: Tasks yield control during IO

## Key Concepts
- **Non-blocking Sockets**: Sockets that don't block on read/write
- **Selectors**: Multiplex IO operations
- **Event Loops**: Schedule and run async tasks
- **Coroutines**: Functions that can be paused and resumed

## Built-in Async IO
```python
import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()}')

    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client('Hello World!'))
```

## File IO (aiofiles)
```python
import aiofiles

async def async_file_operations():
    # Writing
    async with aiofiles.open('example.txt', 'w') as f:
        await f.write('Hello World')

    # Reading
    async with aiofiles.open('example.txt', 'r') as f:
        content = await f.read()
        print(content)
```

## HTTP Requests (aiohttp)
```python
import aiohttp

async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch_url(session, url))

        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results

async def fetch_url(session, url):
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as e:
        return f"Error fetching {url}: {e}"
```

## Database Operations
```python
import asyncpg

async def async_database_operations():
    conn = await asyncpg.connect(user='user', password='password',
                                 database='database', host='127.0.0.1')

    # Execute query
    result = await conn.fetch('SELECT * FROM users WHERE active = $1', True)

    # Insert data
    await conn.execute('''
        INSERT INTO users(name, email) VALUES($1, $2)
    ''', 'John Doe', 'john@example.com')

    await conn.close()
    return result
```

## Performance Benefits
- **Concurrency**: Handle thousands of connections
- **Resource Efficiency**: No thread per connection
- **Scalability**: Better resource utilization
- **Responsiveness**: No blocking operations

## Error Handling
```python
async def robust_async_io():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('http://example.com') as response:
                if response.status == 200:
                    return await response.text()
                else:
                    raise Exception(f"HTTP {response.status}")
    except aiohttp.ClientError as e:
        print(f"Network error: {e}")
        raise
    except asyncio.TimeoutError:
        print("Request timed out")
        raise
```

## Best Practices
- Use appropriate async libraries
- Handle timeouts and errors
- Limit concurrent operations
- Use connection pooling
- Monitor resource usage
- Test with realistic loads
