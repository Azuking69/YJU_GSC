import asyncio
import time

async def test(name):
    print(f"{name} is started")
    await asyncio.sleep(2)
    print(f"{name} is finished")

async def main():
    print("hello world")

if __name__ == "__main__":
    asyncio.run(main()) # EL system start