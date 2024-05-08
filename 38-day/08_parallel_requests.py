# 08_parallel_requests.py
# Sending multiple async requests concurrently

import asyncio
import aiohttp

urls = [
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://jsonplaceholder.typicode.com/todos/2",
    "https://jsonplaceholder.typicode.com/todos/3",
]

async def fetch(url, session):
    async with session.get(url) as resp:
        return await resp.json()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session) for url in urls]
        results = await asyncio.gather(*tasks)
        print(results)

asyncio.run(main())
