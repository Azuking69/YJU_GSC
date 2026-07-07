import asyncio
import time

async def make_order(item, taken_time):
    print(f"{item} 접수")
    await asyncio.sleep(taken_time)
    print(f"{item} 준비완료")

async def main():
    start_time = time.time()
    result1 = asyncio.create_task(make_order("라떼", 3))
    result2 = asyncio.create_task(make_order("아아", 2))
    result3 = asyncio.create_task(make_order("우유", 1))

    # result = await asyncio.gather(make_order("라떼", 3), make_order("아아", 2), make_order("우유", 1))

    elapsed_time = time.time() - start_time
    print(f"{result1}\n{result2}\n{result3}")
    print(f"총 소요시간: {elapsed_time}")

if __name__ == "__main__":
    asyncio.run(main()) # EL system start