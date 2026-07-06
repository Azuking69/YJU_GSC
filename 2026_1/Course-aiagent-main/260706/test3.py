import asyncio
import time

async def make_order(item, taken_time):
    print(f"{item} 준비 시작")
    await asyncio.sleep(taken_time)
    print(f"{item} 준비완료")

async def main():
    ...

if __name__ == "__main__":
    asyncio.run(main()) # EL system start