"""
Chapter 4-3: MCP 도구를 LLM이 실제로 사용하는 최소 1사이클

Chapter 3의 Tool Use 루프에서 "도구 구현"만 MCP 서버로 분리한 형태입니다.
Ch4에서 배울 모든 것이 결국 이 흐름을 위해 존재합니다 - 핵심을 먼저 봅니다.

전체 흐름 (5단계):
    [1] MCP 서버 연결 + list_tools        - 도구 목록 확보
    [2] MCP -> Claude tools 형식 변환      - inputSchema -> input_schema
    [3] 1차 LLM 호출                       - Claude가 tool_use 블록으로 "실행 요청서" 작성
    [4] session.call_tool()                - 실행은 MCP 서버가 (LLM은 실행하지 않는다)
    [5] tool_result 회신 + 2차 LLM 호출    - 결과를 읽고 최종 자연어 답변

실행:
    python chapter4/examples/03_tool_cycle_client.py
"""

import asyncio
import sys
from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()
MODEL = "claude-sonnet-4-6"
SERVER_PATH = str(Path(__file__).parent / "03_tool_cycle_server.py")


async def main():
    llm = Anthropic()
    params = StdioServerParameters(command=sys.executable, args=[SERVER_PATH])

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # [1] 서버가 제공하는 도구 목록을 받습니다.
            listed = await session.list_tools()

            # [2] Claude API 형식으로 변환합니다.
            #     쓰는 필드는 셋뿐: name / description / inputSchema
            #     필드명 주의: MCP는 inputSchema(camelCase), Claude는 input_schema(snake_case)
            tools = [
                {"name": t.name, "description": t.description, "input_schema": t.inputSchema}
                for t in listed.tools
            ]
            print(f"[1-2] MCP 도구 {len(tools)}개 발견: {[t['name'] for t in tools]}")

            messages = [{"role": "user", "content": "글로벌시스템융합과 학번 12번 학생의 성적은?"}]
            print(f"[질문] {messages[0]['content']}")

            # [3] 1차 호출: Claude가 질문을 보고 도구 사용을 스스로 결정합니다.
            #     stop_reason이 "tool_use"로 멈춥니다 - 답변 완료가 아니라 실행 요청 상태.
            rsp = llm.messages.create(model=MODEL, max_tokens=1000, messages=messages, tools=tools)
            messages.append({"role": "assistant", "content": rsp.content})

            for block in rsp.content:
                if block.type == "text":
                    print(f"[3] Claude: {block.text}")
                elif block.type == "tool_use":
                    print(f"[3] 도구 실행 요청: {block.name}({block.input})")

                    # [4] 실행은 MCP 서버가 합니다. LLM은 "요청서"를 썼을 뿐입니다.
                    tool_rsp = await session.call_tool(block.name, block.input)
                    result_text = tool_rsp.content[0].text
                    print(f"[4] MCP 서버 실행 결과: {result_text}")

                    # [5] tool_result로 결과를 돌려줍니다.
                    #     tool_use_id: 어느 요청의 결과인지 매칭 (병렬 호출 대비)
                    messages.append({
                        "role": "user",
                        "content": [{
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result_text,
                            "is_error": tool_rsp.isError or False,
                        }],
                    })

            # [5] 2차 호출: 이번에도 tools를 반드시 함께 보냅니다.
            #     빼면 히스토리의 tool_use/tool_result 블록이 무시되어
            #     "성적 정보에 접근할 수 없습니다" 같은 답이 돌아옵니다.
            final = llm.messages.create(model=MODEL, max_tokens=1000, messages=messages, tools=tools)
            print(f"[5] 최종 답변: {final.content[0].text}")

            # 참고: 도구를 여러 번 연달아 쓰는 일반형은
            #       while rsp.stop_reason == "tool_use": 루프가 필요합니다.
            #       -> 07_agent_with_mcp.py에서 완성합니다.


if __name__ == "__main__":
    asyncio.run(main())
