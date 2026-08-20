"""
Chapter 4-4: Resource 최소 클라이언트

MCP 클라이언트의 최소 골격 4단계만 담았습니다.
    1) stdio_client()      - 서버 프로세스 실행 + stdin/stdout 파이프 연결
    2) ClientSession()     - JSON-RPC 요청/응답 세션
    3) initialize()        - 핸드셰이크 (버전 협상, capabilities 교환)
    4) list_resources() -> read_resource(uri)   - Resource 목록 조회와 읽기

실행:
    python chapter4/examples/04_resource_client.py
"""

import asyncio
import sys
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

SERVER_PATH = str(Path(__file__).parent / "04_resource_server.py")


async def main():
    params = StdioServerParameters(command=sys.executable, args=[SERVER_PATH])

    async with stdio_client(params) as (read, write):          # 1) Transport
        async with ClientSession(read, write) as session:      # 2) Session
            init = await session.initialize()                  # 3) Handshake
            print("서버        :", init.serverInfo.name)
            print("instructions:", init.instructions)

            # 4) Resource 목록을 받아 URI로 하나씩 읽습니다.
            resources = await session.list_resources()
            for r in resources.resources:
                print(f"\n[Resource] {r.uri}  ({r.name})")
                result = await session.read_resource(r.uri)
                print("  내용:", result.contents[0].text)

            # 참고: Tool을 하나도 등록하지 않았지만 capabilities.tools는 존재하고,
            #       tools/list는 빈 목록을 돌려줍니다.
            #       capability = "이 기능군을 지원한다", list = "실제 등록된 목록"
            print("\ncapabilities.tools:", init.capabilities.tools)
            print("tools/list        :", (await session.list_tools()).tools)


if __name__ == "__main__":
    asyncio.run(main())
