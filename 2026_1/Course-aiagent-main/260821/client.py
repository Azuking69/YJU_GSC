import asyncio
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import (
    CreateMessageResult,
    ElicitResult,
    ListRootsResult,
    Root,
    TextContent
)
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
SERVER_PATH = str(Path(__file__).parent / "02_connection_server.py")

server_params = StdioServerParameters(
    command=sys.executable,
    # 실행하고자 하는 서버
    args=[SERVER_PATH],
)


async def main():
    llm_client = Anthropic();
    # stdクライアント
    async with stdio_client(server_params) as (read, write):
        # 서버와 연결된 클라이언트 세션
        async with ClientSession(read, write) as session:
            result = await session.initialize()

            # 현제 MCP 서버에서 제공하는 함수(tool)의 목록을 반환
            # 목록은 Json Schema
            # -함수이름, 매개변수 구조, 설명글(LLM)
            result = await session.list_tools();

            tool_list = [
                            {
                                "name": t.name, 
                                "description": t.description, 
                                "input_schema": t.inputSchema
                            } 
                            for t in result.tools
                        ]

            for tool in result.tools:
                print(tool)
                print()

            promts = [{"role": "user", "content": "글로벌시스템융합과 학번 1의 성적 학생의 GPA는?"}]

            result = llm_client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1000,
                messages=promts,
                tools=tool_list,
            )


            print(result.stop_reason)
            for cnt, block in enumerate(result.content):
                print(f"{cnt} th block ")
                print(block); print()


if __name__ == "__main__":
    asyncio.run(main())