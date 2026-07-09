import asyncio
import time
from anthropic import AsyncAnthropic
from dotenv import load_dotenv

load_dotenv()
sem = asyncio.Semaphore(3)  # 동시 호출 제한
async def call_llm(client: AsyncAnthropic, prompt:str)->str:
    async with sem:
        try:
            # send prompt
            rsp = await client.messages.create(
                model="claude-haiku-4-5",
                max_tokens=200,
                messages=[{"role": "user", "content": prompt}]
            )
            return rsp.content[0]
        
        except Exception as e:
            print(f"예외 발생: {e}")

    """
    LLM 호출
    1) 성공
        결과 값 포맷 검증
        결과 값 반환
    2) 실패
        예외 처리

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