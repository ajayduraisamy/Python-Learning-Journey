# 03_async_tasks.py
# Creating explicit asyncio tasks

import asyncio

async def work(id):
    print(f"Task {id} started")
    await asyncio.sleep(1)
    print(f"Task {id} finished")

async def main():
    tasks = [asyncio.create_task(work(i)) for i in range(3)]
    await asyncio.gather(*tasks)

asyncio.run(main())
