"""
05 ASYNC CONTEXT MANAGERS — EXERCISES

Instructions:
- Create and use async context managers for resource management
- Implement proper setup and cleanup in async contexts
"""

import asyncio
from contextlib import asynccontextmanager

# Exercise 1: Create an async database connection context manager
class AsyncDatabaseConnection:
    """Async context manager for database connections"""

    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None

    async def __aenter__(self):
        # Simulate connection setup
        print(f"Connecting to database: {self.connection_string}")
        await asyncio.sleep(0.1)  # Simulate connection time
        self.connection = f"Connection to {self.connection_string}"
        print("Database connection established")
        return self.connection

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # Simulate connection cleanup
        print("Closing database connection")
        await asyncio.sleep(0.05)  # Simulate cleanup time
        self.connection = None
        print("Database connection closed")

# Exercise 2: Create an async file handler context manager
class AsyncFileHandler:
    """Async context manager for file operations"""

    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    async def __aenter__(self):
        # Simulate file opening
        print(f"Opening file: {self.filename} in mode {self.mode}")
        await asyncio.sleep(0.05)  # Simulate file open time
        self.file = f"File object for {self.filename}"
        print("File opened successfully")
        return self.file

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # Simulate file closing
        print("Closing file")
        await asyncio.sleep(0.02)  # Simulate file close time
        self.file = None
        print("File closed successfully")

# Exercise 3: Use the @asynccontextmanager decorator
@asynccontextmanager
async def async_timer(description):
    """Async context manager that times operations"""
    print(f"Starting: {description}")
    start_time = asyncio.get_event_loop().time()
    try:
        yield
    finally:
        end_time = asyncio.get_event_loop().time()
        duration = end_time - start_time
        print(f"Finished: {description} (took {duration:.3f}s)")

# Exercise 4: Create a resource pool context manager
class AsyncResourcePool:
    """Async context manager for resource pooling"""

    def __init__(self, max_resources=3):
        self.max_resources = max_resources
        self.available_resources = max_resources
        self.waiting = []

    async def __aenter__(self):
        while self.available_resources <= 0:
            # Wait for a resource to become available
            future = asyncio.Future()
            self.waiting.append(future)
            await future

        self.available_resources -= 1
        resource_id = f"Resource-{self.max_resources - self.available_resources}"
        print(f"Acquired {resource_id}")
        return resource_id

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.available_resources += 1
        print(f"Released resource, {self.available_resources} available")

        # Wake up waiting tasks
        if self.waiting:
            future = self.waiting.pop(0)
            future.set_result(None)

# Exercise 5: Use multiple async context managers together
async def demonstrate_nested_contexts():
    """Demonstrate using multiple async context managers"""
    async with AsyncDatabaseConnection("postgresql://localhost/mydb") as db_conn:
        print(f"Using database: {db_conn}")

        async with AsyncFileHandler("data.txt", "w") as file:
            print(f"Writing to file: {file}")

            async with async_timer("File operation"):
                # Simulate some work
                await asyncio.sleep(0.1)
                print("Data written successfully")

        print("File operation completed")

    print("Database operation completed")

if __name__ == "__main__":
    # Run the async demonstrations
    asyncio.run(demonstrate_nested_contexts())

    print("\nDemonstrating resource pool:")
    async def use_resource_pool():
        pool = AsyncResourcePool(max_resources=2)

        async def worker(worker_id):
            async with pool:
                print(f"Worker {worker_id} is using resource")
                await asyncio.sleep(0.2)
                print(f"Worker {worker_id} finished")

        # Create more tasks than available resources
        tasks = [asyncio.create_task(worker(i)) for i in range(4)]
        await asyncio.gather(*tasks)

    asyncio.run(use_resource_pool())
