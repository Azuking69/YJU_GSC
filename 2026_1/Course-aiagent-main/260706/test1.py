import asyncio
import time

async def cr_task1():
    print("A"); await asyncio.sleep(2);
    print("B"); await asyncio.sleep(2); print("C")

async def cr_task2():
    print("F is started"); await asyncio.sleep(2);
    print("F is finished")

async def cr_task3():
    print("G is started"); await asyncio.sleep(2);
    print("G is finished")


async def main():
    task1 = asyncio.create_task(cr_task1()) #task1
    task2 = asyncio.create_task(cr_task2()) #task2
    task3 = asyncio.create_task(cr_task3()) #task3

    await task1, task2, task3

if __name__ == "__main__":
    asyncio.run(main())