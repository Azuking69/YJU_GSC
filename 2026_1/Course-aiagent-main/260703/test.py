import time
import asyncio

async def make_order(menu:str, taken_time:int)->str: # 비동기 함수 정의
    print(f"{menu} 준비중")
    await asyncio.sleep(taken_time) # 비동기 함수 호출, wait
    return f"{menu} 준비 완료"

async def main():
    start = time.time()
    result1 = asyncio.create_task(make_order("라떼", 3)) # Task 객체 생성, wait
    result2 = asyncio.create_task(make_order("아아", 2)) # Task 객체 생성, wait
    result3 = asyncio.create_task(make_order("우유", 1)) # Task 객체 생성, wait
    
    await result1
    await result2
    await result3
    print(result1, result2, result3)

    elasped_time = time.time() - start

    print(f"경과 시간 {elasped_time}")

if __name__ == "__main__":
    asyncio.run(main()) # create event loop