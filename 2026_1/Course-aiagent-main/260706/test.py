import asyncio
import time

async def test(name):
    print(f"{name} is started")
    await asyncio.sleep(2)
    print(f"{name} is finished")

async def main():
    # task1
    task1 = asyncio.create_task(test(1)) # return -> task
    # task 2
    task2 = asyncio.create_task(test(2)) # return -> task

    await task1, task2

    print("프로그램 종료")

if __name__ == "__main__":
    asyncio.run(main()) # EL system start