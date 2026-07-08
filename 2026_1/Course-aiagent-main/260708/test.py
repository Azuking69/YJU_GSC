import asyncio
import time
from anthropic import AsyncAnthropic

async def ask(client: AsyncAnthropic, prompt: str) -> str:
    client.messages.create(
        model = "claude-haiku-4-5-20251001",
        max_tokens = 200,
        messages = [{"role":"user", "content":prompt}],
    )
    return rsp.content[0]

async def main():
    client = AsyncAnthropic()

    start_time = time.time()
    ask(client, "파이썬은 뭐야?")
    elapsed_time = time.time() - start_time
    print(f"총 소요시간: {elapsed_time}")

if __name__ == "__main__":
    asyncio.run(main())