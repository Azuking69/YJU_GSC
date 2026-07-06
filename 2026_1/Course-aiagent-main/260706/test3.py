import asyncio
import time

async def make_order(item, taken_time):
    print(f"{item} 접수")
    await asyncio.sleep(taken_time)
    print(f"{item} 준비완료")

async def main():
    await make_order("라떼", 3)
    await make_order("아아", 2)
    await make_order("우유", 1)

if __name__ == "__main__":
    asyncio.run(main()) # EL system start