from typing import TypedDict
from langgraph.graph import State, START, END

class State(TypeedDict):
    name: str
    msg: str

def my_node(state: State):
    ...