
def run():
    print("=== 02 ASYNC AWAIT SYNTAX Examples ===
")

    import asyncio

    # Example 1: Basic async function
    print("1. Basic Async Function:")
    print("   async def hello():")
    print("       await asyncio.sleep(1)")
    print("       return 'Hello, Async!'")
    print()
    print("   result = asyncio.run(hello())")
    print("   print(result)")

    print()

    # Example 2: Concurrent tasks
    print("2. Concurrent Tasks:")
    print("   async def main():")
    print("       tasks = [asyncio.create_task(task()) for task in task_list]")
    print("       results = await asyncio.gather(*tasks)")
    print("       return results")

    print()

    # Example 3: Async context manager
    print("3. Async Context Manager:")
    print("   async with aiofiles.open('file.txt', 'r') as f:")
    print("       content = await f.read()")

if __name__ == "__main__":
    run()
