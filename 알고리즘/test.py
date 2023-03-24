import asyncio
import time


async def main():
    print("hello")
    time.sleep(1)
    print("world")


asyncio.run(main())

print(1)
