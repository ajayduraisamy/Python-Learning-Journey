# 06_aiohttp_get.py
# aiohttp GET request example

import asyncio
import aiohttp

async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/todos/1") as resp:
            data = await resp.json()
            print(data)

asyncio.run(fetch())
