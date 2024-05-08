# 01_async_basic.py
# Basic async/await example

import asyncio

async def hello():
    print("Hello...")
    await asyncio.sleep(1)
    print("World!")

asyncio.run(hello())
