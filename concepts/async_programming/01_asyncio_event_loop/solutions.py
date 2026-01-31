# Asyncio Event Loop Exercises Solutions

import asyncio

async def hello(name):
    print(f"Hello {name}")
    await asyncio.sleep(1)
    print(f"Bye {name}")

async def main():
    await asyncio.gather(hello("Alice"), hello("Bob"))

asyncio.run(main())