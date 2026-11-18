from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from dataclasses import dataclass


# State
State1: dict[str, str|int] = {"msg": "", "age": 2}

# TypedDict
class State2(TypedDict):
    "msg": str

# dataclass
@dataclass
class State3:
    msg: int = ""