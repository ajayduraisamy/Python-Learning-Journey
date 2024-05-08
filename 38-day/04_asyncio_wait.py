# 04_asyncio_wait.py
# Using asyncio.wait with FIRST_COMPLETED

import asyncio

async def long_task(n):
    await asyncio.sleep(n)
    return f"Finished {n}s"

async def main():
    tasks = [asyncio.create_task(long_task(t)) for t in [1,3,5]]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print("First completed:", [d.result() for d in done])

asyncio.run(main())
