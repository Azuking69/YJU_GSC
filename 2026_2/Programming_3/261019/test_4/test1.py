from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.state import CompiledStateGraph

# ================ State structures =================
class State(TypedDict):
    dept: str
    msg: str

class StateNameResult(TypedDict):
    dept: str

class StateMsgResult(TypedDict):
    msg: str

# ================= Add Nodes =================
def addName(state: State) -> dict[str, str]:
    return {"dept": "gsc"}

def addMsg(state: State) -> dict[str, str]:
    return {"msg": "님 안녕하세요"}


# ================= Graph =================
pre_graph: StateGraph[State] = StateGraph(State)

pre_graph.add_node("dept", addName)
pre_graph.add_node("msg", addMsg)

pre_graph.add_edge(START, "dept")
pre_graph.add_edge("dept", "msg")
pre_graph.add_edge("msg", END)

# ================= Compile and Invoke =================
my_graph: CompiledStateGraph = pre_graph.compile()
result: dict[str, str] = my_graph.invoke({"dept": "", "msg": ""})

print(result)  # {'name': 'gsc', 'msg': '님 안녕하세요'}