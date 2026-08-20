import asyncio
import json
import sys
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

SERVER_PATH = str(Path(__file__).parent / "02_connection_server.py")

server_params = StdioServerParameters(
    command=sys.executable,
    # 실행하고자 하는 서버
    args=["SERVER_PATH"],
)


async def main():
    # stdクライアント
    async with stdio_client(server_params) as (read, write):
        # 서버와 연결된 클라이언트 세션
        async with ClientSession(read, write) as session:
            result = await session.initialize()

            # 현제 MCP 서버에서 제공하는 함수(tool)의 목록을 반환
            # 목록은 Json Schema
            # -함수이름, 매개변수 구조, 설명글(LLM)
            result = await session.list_tools();

            for tool in result.tools:
                print(tool)
                print()
            dump("Discover result for tools", result)



if __name__ == "__main__":
    asyncio.run(main())