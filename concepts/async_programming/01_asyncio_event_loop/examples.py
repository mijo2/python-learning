# Asyncio Event Loop Examples

import asyncio

async def task(name, delay):
    print(f"Task {name} starting")
    await asyncio.sleep(delay)
    print(f"Task {name} done")

async def main():
    await asyncio.gather(task("A", 1), task("B", 2), task("C", 1))

asyncio.run(main())  # Runs concurrently, total ~2s