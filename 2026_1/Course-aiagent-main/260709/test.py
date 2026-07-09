import asyncio
import time
from anthropic import AsyncAnthropic
from dotenv import load_dotenv

load_dotenv()

sem = asyncio.Semaphore(3)  # 동시 호출 제한

# LLM 호출
async def call_llm(client: AsyncAnthropic, prompt:str, max_retries:int=3, delay:int=3)->str:
    for attempt in range(max_retries):
        async with sem:
            # 1) 성공
            #    결과 값 포맷 검증
            try:
                # send prompt
                rsp = await client.messages.create(
                    model="claude-haiku-4-5",
                    max_tokens=200,
                    messages=[{"role": "user", "content": prompt}]
                )
                # 결과 값 반환
                return rsp.content[0]
            
            # 2) 실패
            #    예외 처리        
            except Exception as e:
                print(f"예외 발생: {e}")
                # 즉시 예외 발생: 모델명을 잘 못 선택

                # 재전송

                if attempt >= max_retries - 1:
                    print("최대 재시도 횟수 초과. 실패 처리.")
                    return Exception
                
                await asyncio.sleep(delay)  # 재시도 전 대기

    """
    
    
        


    if 결과 값 검증 실패 or 예외 발생(재시도)
        재전송
    """
    ...

async def main():
    # LLM 호출
    client = AsyncAnthropic()

    # Promt
    task1 = asyncio.create_task(call_llm(client, "파이썬은 뭐야?"))
    task2 = asyncio.create_task(call_llm(client, "영진전문대 주소는?"))

    result1, result2 = await task1, await task2
    print(result1, "\n\n", result2)
    ...

if __name__ == "__main__":
    asyncio.run(main())