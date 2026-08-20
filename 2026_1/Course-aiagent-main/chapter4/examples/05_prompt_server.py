"""
Chapter 4-5: Prompt 최소 서버

Tool/Resource 없이 Prompt 하나만 노출하는 가장 작은 MCP 서버입니다.
    - Prompt: explain(topic, level)   - 주제 설명 요청 템플릿

Prompt는 "사용자가 골라서 실행하는" 재사용 대화 템플릿입니다.
서버는 인자를 받아 완성된 메시지를 돌려줄 뿐, LLM을 직접 호출하지 않습니다.

직접 실행하지 않아도 05_prompt_client.py가 자식 프로세스로 자동 실행합니다.
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("prompt-demo")


# 인자 정보는 함수 시그니처에서 추출됩니다. (Prompt 인자는 모두 문자열)
#   - 기본값 없음  -> required=True   (topic)
#   - 기본값 있음  -> required=False  (level)
# docstring은 프롬프트 설명(description)으로 전달됩니다.
@mcp.prompt()
def explain(topic: str, level: str = "초급") -> str:
    """주제를 학습자 수준(초급/중급/고급)에 맞게 설명해 달라는 프롬프트를 만듭니다."""
    return f"당신은 친절한 강사입니다. '{topic}'을(를) {level} 학습자에게 3문장으로 설명하세요."


if __name__ == "__main__":
    mcp.run()
