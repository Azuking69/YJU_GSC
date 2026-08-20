"""
Chapter 4-5: Prompt 최소 클라이언트

Prompt를 다루는 두 메서드만 봅니다.
    1) list_prompts()              - 어떤 프롬프트가 있고 어떤 인자를 받는지 조회
    2) get_prompt(name, arguments) - 인자를 채워 완성된 messages 받기

반환된 messages는 그대로 Claude API의 messages 파라미터로 넘길 수 있습니다.
(07_agent_with_mcp.py에서 실제로 LLM과 연결합니다)

실행:
    python chapter4/examples/05_prompt_client.py
"""

import asyncio
import sys
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

SERVER_PATH = str(Path(__file__).parent / "05_prompt_server.py")


async def main():
    params = StdioServerParameters(command=sys.executable, args=[SERVER_PATH])

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 1) 프롬프트 목록: 이름, 설명, 인자(필수 여부)
            prompts = await session.list_prompts()
            for p in prompts.prompts:
                args = ", ".join(f"{a.name}{'' if a.required else '?'}" for a in p.arguments or [])
                print(f"[Prompt] {p.name}({args})")
                print(f"  설명: {p.description}")

            # 2) 인자를 채워 완성된 메시지를 받습니다. (인자 값은 모두 문자열)
            result = await session.get_prompt("explain", arguments={"topic": "MCP", "level": "초급"})
            print("\n[get_prompt 결과]")
            for m in result.messages:
                print(f"  {m.role}: {m.content.text}")

            # 3) Claude API로 넘길 형태로 변환하면 끝입니다.
            messages = [{"role": m.role, "content": m.content.text} for m in result.messages]
            print("\n[Claude API messages]")
            print(" ", messages)


if __name__ == "__main__":
    asyncio.run(main())
