import asyncio
import random

async def test(num):
    print(f"{num} is started")
    asyncio.sleep(2)

    foo = random.randint(1, 10)
    return foo

async def main():
    print("hello world")
    result1 = asyncio.create_task(test(1))
    result2 = asyncio.create_task(test(2))

    await result1, result2
    print(result1.result(), result2.result())


if __name__ == "__main__":
    asyncio.run(main()) # run(인자값의 자료형은?)
    # create event loop