import asyncio
import time
from anthropic import AsyncAnthropic
from dotenv import load_dotenv

load_dotenv()

sem = asyncio.Semaphore(3)  # 동시에 실행할 수 있는 최대 작업 수를 제한

async def ask(client: AsyncAnthropic, prompt: str) -> str:
    async with sem:  # 세마포어를 사용하여 동시 실행 제한
        rsp = await client.messages.create( # <- await로 비동기 호출
            model = "claude-haiku-4-5-20251001",
            max_tokens = 200,
            messages = [{"role":"user", "content":prompt}],
        )
        return rsp.content[0].text

async def main():
    client = AsyncAnthropic()
    prompts = ["파이썬은 뭐야?", "한국의 수도는?", "영진전문대 주소는?"]
    start_time = time.time()
    results = await asyncio.gather(
        *[ask(client, prompt) for prompt in prompts]
    )
    

    for result in results:
        print(result)
        print("*" * 50)
    elapsed_time = time.time() - start_time
    print(f"총 소요시간: {elapsed_time}")

if __name__ == "__main__":
    asyncio.run(main()) 