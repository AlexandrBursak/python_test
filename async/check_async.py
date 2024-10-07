import asyncio

async def coro(sleep_time):
    print(f"Sleeping for {sleep_time} seconds")
    await asyncio.sleep(sleep_time)
    print(f"Done sleeping for {sleep_time} seconds")


async def main():
    c1 = coro(1)
    c2 = coro(2)
    c3 = coro(3)

    await asyncio.gather(c1,c2,c3)
    # await c1
    # await c2
    # await c3

asyncio.run(main())