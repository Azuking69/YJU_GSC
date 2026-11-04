from typing import Any, TypedDict, NotRequired, Union, Optional, Literal, Final, Callable
from dataclasses import asdict, dataclass


def add(x:int, y:int) -> int:
    return x + y

def div(x:int, y:int, z:int) -> float:
    return x / y / z

def calc(x:int, y:int, op:Callable[[int, int], float]) -> float:
    return op(x, y)

print(calc(2, 3, add))
print(calc(2, 3, div))