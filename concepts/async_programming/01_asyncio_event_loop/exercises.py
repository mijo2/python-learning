# Asyncio Event Loop Exercises

import asyncio

# Exercise: Create concurrent async tasks

async def hello(name):
    print(f"Hello {name}")
    await asyncio.sleep(1)
    print(f"Bye {name}")

# TODO: Define main() with asyncio.gather for hello("Alice") and hello("Bob")
# Uncomment to run
# asyncio.run(main())