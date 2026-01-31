
def run():
    print("=== 04 FUTURES Examples ===\n")

    import asyncio

    # Example 1: Creating and using futures
    print("1. Creating and Using Futures:")

    async def create_future_example():
        # Create a future
        future = asyncio.Future()

        # Set result asynchronously
        async def set_result():
            await asyncio.sleep(0.1)
            future.set_result("Future completed!")

        # Start the task
        asyncio.create_task(set_result())

        # Wait for the result
        result = await future
        return result

    # Run the example
    result = asyncio.run(create_future_example())
    print(f"Future result: {result}")

    print()

    # Example 2: Concurrent tasks with asyncio.gather
    print("2. Concurrent Tasks with asyncio.gather:")

    async def concurrent_tasks_example():
        async def worker(task_id, delay):
            print(f"Starting task {task_id}")
            await asyncio.sleep(delay)
            print(f"Completed task {task_id}")
            return f"Result from task {task_id}"

        # Create multiple tasks
        tasks = [
            asyncio.create_task(worker(1, 0.5)),
            asyncio.create_task(worker(2, 0.3)),
            asyncio.create_task(worker(3, 0.7))
        ]

        # Wait for all to complete
        results = await asyncio.gather(*tasks)
        return results

    # Run the concurrent tasks
    results = asyncio.run(concurrent_tasks_example())
    print(f"All results: {results}")

    print()

    # Example 3: Future callbacks
    print("3. Future Callbacks:")

    def on_future_done(future):
        print(f"Future callback: {future.result()}")

    async def callback_example():
        future = asyncio.Future()
        future.add_done_callback(on_future_done)

        # Complete the future
        await asyncio.sleep(0.1)
        future.set_result("Callback triggered!")

        # Wait a bit for callback to execute
        await asyncio.sleep(0.01)

    asyncio.run(callback_example())

    print()

    # Example 4: Exception handling in futures
    print("4. Exception Handling in Futures:")

    async def exception_example():
        future = asyncio.Future()

        async def fail_task():
            await asyncio.sleep(0.1)
            future.set_exception(ValueError("Task failed!"))

        asyncio.create_task(fail_task())

        try:
            result = await future
        except ValueError as e:
            print(f"Caught exception: {e}")
            return "Exception handled"

    result = asyncio.run(exception_example())
    print(f"Exception handling result: {result}")

if __name__ == "__main__":
    run()
