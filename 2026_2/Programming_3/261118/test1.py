from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from dataclasses import dataclass


# State
State1: dict[str, str|int] = {"msg": 2, "age": ""}   # {"msg": "", "age": 2}

# TypedDict
class State2(TypedDict):
    "msg": str
    "arg": int

# dataclass
@dataclass
class State3:
    msg: str = ""
    age: int = 0