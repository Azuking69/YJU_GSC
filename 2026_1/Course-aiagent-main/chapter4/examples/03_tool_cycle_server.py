"""
Chapter 4-3: 도구 호출 1사이클 서버

LLM 결합 흐름의 핵심만 보기 위해 Tool 하나만 노출하는 최소 서버입니다.

직접 실행하지 않아도 03_tool_cycle_client.py가 자식 프로세스로 자동 실행합니다.
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("score-server")

# 실습용 성적 데이터입니다. 실제라면 DB나 학사 API를 조회하겠지만,
# 핵심은 "이 로직이 Agent 코드 밖(MCP 서버)에 있다"는 점입니다.
SCORES = {7: 85, 12: 100, 25: 91}


@mcp.tool()
def get_score(id: int) -> str:
    """글로벌시스템융합과 학생의 성적을 조회합니다.

    Args:
        id: 학생의 학번
    """
    if id not in SCORES:
        return f"학번 {id}번 학생을 찾을 수 없습니다."
    return f"학번 {id}번 학생의 성적은 {SCORES[id]}점입니다."


if __name__ == "__main__":
    mcp.run()
