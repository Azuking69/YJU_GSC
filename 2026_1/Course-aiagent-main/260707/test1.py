import asyncio
import time
from anthropic import AsyncAnthropic

MODEL = "claud-haiku-4-5-20251001"
async def ask(client: AsyncAnthropic, mas:str)->str:
    response = await client.massage.create( # await로 비동기 호출
        model = MODEL,
        max_token = 100,
        message = [{"role": "user", "content": question}],
    )

    return response.content[0].text
    

async def main():
    start_time = time.time()
    # LLM prompt 전송
    client = AsyncAnthropic()

    result = await asyncio.gather(
        ask(client, "파이썬은 뭐야?"), # "파이썬은 뭐야?"
        ask(client, "자바스크립트는 뭐야?"), # "자바스크립트는 뭐야?"
        ask(client, "GO 언어는 뭐야?"), # "GO 언어는 뭐야?"
    )

    elapsed_time = time.time() - start_time

    for text in result:
        print(text)
        print("*" * 50)
    print(f"총 소요시간: {elapsed_time}")


if __name__ == "__main__":
    asyncio.run(main())