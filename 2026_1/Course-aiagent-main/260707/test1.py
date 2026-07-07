import asyncio
import time
from anthropic import AsysncAnthropic

MODEL = "claud-haiku-4-5-20251001"
async def ask(client: AsysncAnthropic, mas:str)->str:
    response = await client.massage.create( # await로 비동기 호출
        model = MODEL,
        max_token = 100,
        message = [{"role": "user", "content": question}],
        )

async def main():
    # LLM prompt 전송
    client = AsysncAnthropic()
    # "파이썬은 뭐야?"
    result = await ask(client, "파이썬은 뭐야?")
    print(result)
    # "자바스크립트는 뭐야?"
    # "GO 언어는 뭐야?"

if __name__ == "__main__":
    asyncio.run(main())