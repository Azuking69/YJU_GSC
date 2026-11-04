from typing import Any, NoReturn, TypedDict, NotRequired, Union, Optional, Literal, Final, Callable
from dataclasses import asdict, dataclass

def make_exception() -> NoReturn:
    raise ValueError()

def test():
    ...

# print(type(test)) # return値が無くても、functionを返す
print(type(make_exception)) # NoReturnを返す。