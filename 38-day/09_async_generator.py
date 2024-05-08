# 09_async_generator.py
# async generator with yield

import asyncio

async def async_counter():
    for i in range(1, 6):
        await asyncio.sleep(0.2)
        yield i

async def main():
    async for n in async_counter():
        print(n)

asyncio.run(main())
