from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from dataclasses import dataclass


# State
# State1: dict[str, str|int] = {"msg": 2, "age": 0}   # {"msg": "", "age": 2}
State1 = {"msg": "", "age": 0}   # {"msg": "", "age": 2}

# TypedDict
class State2(TypedDict):
    msg: str
    age: int

s2 = State2(msg="gsc", age=10)
print(f"type: {type(s2)}, value: {s2}")


# dataclass
@dataclass
class State3:
    msg: str = ""
    age: int = 0


# START -> T1 -> T2 -> END
def t1(state: State2):
    print("t1")
    return {"msg": "hello"}

def t2(state: State2):
    print("t2")
    return {"age": 20}


builder: StateGraph[State2] = StateGraph(State2)
builder.add_node(t1)
builder.add_node(t2)

builder.add_edge(START, "t1")
builder.add_edge("t1", "t2")
builder.add_edge("t2", END)

graph = builder.compile()
result_1 = graph.invoke({"msg": "gsc", "age": 0})
print(result_1)  # {'msg': 'hello', 'age': 20}