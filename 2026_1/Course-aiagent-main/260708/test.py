import asyncio
import time
from anthropic import AsyncAnthropic

async def ask(client: AsyncAnthropic, prompt: str) -> str:
    ...

async def main():
    client = AsyncAnthropic()

    start_time = time.time()
    ask(client, "파이썬은 뭐야?")
    elapsed_time = time.time() - start_time
    print(f"총 소요시간: {elapsed_time}")

if __name__ == "__main__":
    asyncio.run(main())