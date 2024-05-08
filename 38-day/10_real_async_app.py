# 10_real_async_app.py
# A real async workflow: fetch -> process -> display

import asyncio
import aiohttp

async def fetch_data(session):
    async with session.get("https://jsonplaceholder.typicode.com/users") as resp:
        return await resp.json()

async def process_data(users):
    return [u["name"].upper() for u in users]

async def main():
    async with aiohttp.ClientSession() as session:
        users = await fetch_data(session)
        names = await process_data(users)
        print(names[:5])  # show first 5

asyncio.run(main())
