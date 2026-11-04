from typing import Any, TypedDict, NotRequired, Union, Optional, Literal, Final, Callable
from dataclasses import asdict, dataclass


def add(x:int, y:int) -> int:
    return x + y

def div(x:int, y:int,) -> float:
    return x / y

def calc(x:int, y:int, op) -> float:
    return op(x, y)

print(calc(2, 3, add))
print(calc(2, 3, div))