"""
Chapter 4-4: Resource 최소 서버

Tool 없이 Resource 하나만 노출하는 가장 작은 MCP 서버입니다.
    - Resource: info://about   - 서버 소개 텍스트 (읽기 전용 데이터)

직접 실행하지 않아도 04_resource_client.py가 자식 프로세스로 자동 실행합니다.
"""

from mcp.server.fastmcp import FastMCP

# instructions는 initialize 응답에 실려 클라이언트(LLM)에게 전달되는 사용 안내문입니다.
mcp = FastMCP(
    "resource-demo",
    instructions="이 서버는 소개 정보를 Resource로만 제공합니다. 도구는 없습니다.",
)


@mcp.resource("info://about")
def about() -> str:
    """이 서버의 소개 문구를 반환합니다."""
    return "resource-demo 서버입니다. Resource는 Host 앱이 필요할 때 URI로 읽어 가는 데이터입니다."


if __name__ == "__main__":
    mcp.run()
