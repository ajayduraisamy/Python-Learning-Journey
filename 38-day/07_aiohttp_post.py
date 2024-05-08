# 07_aiohttp_post.py
# aiohttp POST request example

import asyncio
import aiohttp

async def send():
    payload = {"name": "Ajay", "msg": "Async rocks!"}
    async with aiohttp.ClientSession() as session:
        async with session.post("https://httpbin.org/post", json=payload) as resp:
            print(await resp.json())

asyncio.run(send())
