# 05_asyncio_timeout.py
# asyncio timeout wrapper

import asyncio

async def slow():
    await asyncio.sleep(3)
    return "Done"

async def main():
    try:
        result = await asyncio.wait_for(slow(), timeout=1)
        print(result)
    except asyncio.TimeoutError:
        print("Task timed out!")

asyncio.run(main())
